from collections import OrderedDict

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field, inline_serializer
from rest_framework import serializers

from api.v1.v1_forms.constants import QuestionTypes, FormTypes
from api.v1.v1_forms.models import Forms, QuestionGroup, Questions, \
    QuestionOptions, FormApprovalRule
from api.v1.v1_profile.models import Administration, Levels
from api.v1.v1_users.models import SystemUser
from rtmis.settings import FORM_GEO_VALUE
from utils.custom_serializer_fields import CustomChoiceField, \
    CustomPrimaryKeyRelatedField, CustomListField


class ListOptionSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        result = super(ListOptionSerializer, self).to_representation(
            instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None])

    class Meta:
        model = QuestionOptions
        fields = ['id', 'name', 'order']


class ListQuestionSerializer(serializers.ModelSerializer):
    option = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    center = serializers.SerializerMethodField()

    @extend_schema_field(ListOptionSerializer(many=True))
    def get_option(self, instance: Questions):
        if instance.type in [QuestionTypes.administration,
                             QuestionTypes.cascade]:
            return QuestionTypes.FieldStr.get(
                QuestionTypes.administration).lower()
        if instance.type in [QuestionTypes.geo,
                             QuestionTypes.administration,
                             QuestionTypes.option,
                             QuestionTypes.multiple_option]:
            return ListOptionSerializer(
                instance=instance.question_question_options.all(),
                many=True).data
        return None

    @extend_schema_field(OpenApiTypes.STR)
    def get_type(self, instance: Questions):
        if instance.type == QuestionTypes.administration:
            return QuestionTypes.FieldStr.get(QuestionTypes.cascade).lower()
        return QuestionTypes.FieldStr.get(instance.type).lower()

    @extend_schema_field(inline_serializer('center',
                                           fields={
                                               'lat': serializers.FloatField(),
                                               'lng': serializers.FloatField(),
                                           }))
    def get_center(self, instance: Questions):
        if instance.type == QuestionTypes.geo:
            return FORM_GEO_VALUE
        return None

    def to_representation(self, instance):
        result = super(ListQuestionSerializer, self).to_representation(
            instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None])

    class Meta:
        model = Questions
        fields = ['id', 'name', 'order', 'type', 'required',
                  'dependency', 'option', 'center', 'meta']


# TODO: confirm Order in QuestionGroup model
class ListQuestionGroupSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    @extend_schema_field(ListQuestionSerializer(many=True))
    def get_question(self, instance: QuestionGroup):
        return ListQuestionSerializer(
            instance=instance.question_group_question.all().order_by('order'),
            many=True).data

    class Meta:
        model = QuestionGroup
        fields = ['name', 'question']


class ListAdministrationCascadeSerializer(serializers.ModelSerializer):
    value = serializers.ReadOnlyField(source='id')
    label = serializers.ReadOnlyField(source='name')
    children = serializers.SerializerMethodField()

    @extend_schema_field(inline_serializer('children', fields={
        'value': serializers.IntegerField(),
        'label': serializers.CharField(),
    }, many=True))
    def get_children(self, instance: Administration):
        return ListAdministrationCascadeSerializer(
            instance=instance.parent_administration.all(), many=True
        ).data

    class Meta:
        model = Administration
        fields = ['value', 'label', 'children']


class WebFormDetailSerializer(serializers.ModelSerializer):
    question_group = serializers.SerializerMethodField()
    cascade = serializers.SerializerMethodField()

    @extend_schema_field(ListQuestionGroupSerializer(many=True))
    def get_question_group(self, instance: Forms):
        return ListQuestionGroupSerializer(
            instance=instance.form_question_group.all(), many=True).data

    @extend_schema_field(
        inline_serializer('administration', fields={
            'administrator': ListAdministrationCascadeSerializer(
                many=True)}))
    def get_cascade(self, instance):
        return {'administration': ListAdministrationCascadeSerializer(
            instance=Administration.objects.filter(parent__isnull=True),
            many=True).data}

    class Meta:
        model = Forms
        fields = ['name', 'question_group', 'cascade']


class ListFormRequestSerializer(serializers.Serializer):
    type = CustomChoiceField(choices=list(FormTypes.FieldStr.keys()),
                             required=False)


class ListFormSerializer(serializers.ModelSerializer):
    type_text = serializers.SerializerMethodField()

    def get_type_text(self, instance):
        return FormTypes.FieldStr.get(instance.type)

    class Meta:
        model = Forms
        fields = ['id', 'name', 'type', 'version', 'type_text']


class FormDataListQuestionSerializer(serializers.ModelSerializer):
    option = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    @extend_schema_field(ListOptionSerializer(many=True))
    def get_option(self, instance: Questions):
        if instance.type in [QuestionTypes.geo,
                             QuestionTypes.option,
                             QuestionTypes.multiple_option]:
            return ListOptionSerializer(
                instance=instance.question_question_options.all(),
                many=True).data
        return None

    @extend_schema_field(OpenApiTypes.STR)
    def get_type(self, instance: Questions):
        if instance.type == QuestionTypes.administration:
            return QuestionTypes.FieldStr.get(QuestionTypes.cascade).lower()
        return QuestionTypes.FieldStr.get(instance.type).lower()

    @extend_schema_field(inline_serializer('center',
                                           fields={
                                               'lat': serializers.FloatField(),
                                               'lng': serializers.FloatField(),
                                           }))
    def to_representation(self, instance):
        result = super(FormDataListQuestionSerializer, self).to_representation(
            instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None])

    class Meta:
        model = Questions
        fields = ['id', 'form', 'question_group', 'name', 'order',
                  'meta', 'type', 'required', 'rule', 'option', 'dependency']


class FormDataQuestionGroupSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    @extend_schema_field(FormDataListQuestionSerializer(many=True))
    def get_question(self, instance: QuestionGroup):
        return FormDataListQuestionSerializer(
            instance=instance.question_group_question.all().order_by('order'),
            many=True).data

    class Meta:
        model = QuestionGroup
        fields = ['id', 'name', 'question']


class FormDataSerializer(serializers.ModelSerializer):
    question_group = serializers.SerializerMethodField()

    @extend_schema_field(FormDataQuestionGroupSerializer(many=True))
    def get_question_group(self, instance: Forms):
        return FormDataQuestionGroupSerializer(
            instance=instance.form_question_group.all(), many=True).data

    class Meta:
        model = Forms
        fields = ['id', 'name', 'question_group']


class EditFormTypeSerializer(serializers.ModelSerializer):
    form_id = CustomPrimaryKeyRelatedField(queryset=Forms.objects.none())
    type = CustomChoiceField(choices=list(FormTypes.FieldStr.keys()))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields.get('form_id').queryset = Forms.objects.all()

    def create(self, validated_data):
        form: Forms = validated_data.get('form_id')
        form.type = validated_data.get('type')
        form.save()
        return form

    class Meta:
        model = Forms
        fields = ['form_id', 'type']


class EditFormApprovalSerializer(serializers.ModelSerializer):
    form_id = CustomPrimaryKeyRelatedField(queryset=Forms.objects.none())
    level_id = CustomListField(
        child=CustomPrimaryKeyRelatedField(queryset=Levels.objects.none()))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields.get('form_id').queryset = Forms.objects.all()
        self.fields.get('level_id').child.queryset = Levels.objects.all()

    def create(self, validated_data):
        return object

    class Meta:
        model = FormApprovalRule
        fields = ['form_id', 'level_id']


class ApprovalFormUserSerializer(serializers.Serializer):
    user_id = CustomPrimaryKeyRelatedField(queryset=SystemUser.objects.none())
    administration_id = CustomPrimaryKeyRelatedField(
        queryset=Administration.objects.none())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields.get('user_id').queryset = SystemUser.objects.all()
        self.fields.get(
            'administration_id').queryset = Administration.objects.all()

    def create(self, validated_data):
        print(validated_data)
        print(self.context.get('form'))
        return object
