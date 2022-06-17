import React from "react";
import { Tour } from "../../../components";
import { store, config } from "../../../lib";

const UploadDataTour = () => {
  const { user: authUser } = store.useState((s) => s);

  const steps = [
    ...(config.checkAccess(authUser?.role_detail, "data")
      ? [
          {
            image: "/assets/tour/upload-data/1.png",
            title: "Download",
            description:
              "Lorem ipsum dolor sit, amet consectetur adipisicing elit",
          },
          {
            image: "/assets/tour/upload-data/2.png",
            title: "Upload / Browsing to your computer",
            description:
              "Velit amet omnis dolores. Ad eveniet ex beatae dolorum",
          },
        ]
      : []),
  ];

  return <Tour steps={steps} />;
};

export default React.memo(UploadDataTour);
