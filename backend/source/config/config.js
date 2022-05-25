var visualisation = [
  {
    id: 519630048,
    title: "Household",
    type: 1,
    map: {
      marker: {
        id: 513690068,
        title: "Functional household toilet available",
        options: [
          {
            id: 697,
            name: "No toilet observed",
          },
          {
            id: 698,
            name: "Toilet with inadequate privacy",
          },
          {
            id: 699,
            name: "Toilet not functional",
          },
          {
            id: 700,
            name: "Functional toilet with privacy",
          },
        ],
      },
      shape: {
        id: 519660055,
        title: "Age of the household head",
      },
    },
    chartListTitle: "JMP",
    charts: [
      {
        type: "CRITERIA",
        title: "Sanitation Service Level",
        options: [
          {
            name: "Safely Managed",
            color: "#368541",
            score: 15,
            options: [
              {
                question: 492490054,
                option: [
                  "Flush / pour flush",
                  "Pit latrine with slab",
                  "Twin pit with slab",
                ],
              },
              {
                question: 513690062,
                option: ["No"],
              },
              {
                question: 513690060,
                option: [
                  "Removed by service provider to a treatment plant",
                  "Removed by service provider to buried pit",
                  "Emptied by household buried in a covered pit",
                ],
              },
            ],
          },
          {
            name: "Basic",
            score: 10,
            color: "#79BE7D",
            options: [
              {
                question: 492490054,
                option: [
                  "Flush / pour flush",
                  "Pit latrine with slab",
                  "Twin pit with slab",
                ],
              },
              {
                question: 513690062,
                option: ["No"],
              },
            ],
          },
          {
            name: "Limited",
            score: -1,
            color: "#FDF177",
            options: [
              {
                question: 492490054,
                option: [
                  "Flush / pour flush",
                  "Pit latrine with slab",
                  "Twin pit with slab",
                ],
              },
              {
                question: 513690062,
                option: ["Yes"],
              },
            ],
          },
          {
            name: "Unimproved",
            score: -2,
            color: "#FBD256",
            options: [
              {
                question: 492490054,
                option: [
                  "Pit latrine without slab / Open pit",
                  "Twin pit without slab",
                  "Bucket",
                  "Hanging toilet / hanging latrine",
                ],
              },
            ],
          },
          {
            name: "Open Defecation",
            score: -3,
            // title: "OD",
            color: "#F1AC2A",
            options: [
              {
                question: 492490054,
                option: ["No facility / Bush / Field"],
              },
            ],
          },
        ],
        // stack: {
        //   options: [
        //     {
        //       name: "805",
        //       title: "805, Baringo", // Eg. Override administration name
        //     },
        //   ],
        // },
      },
      {
        type: "ADMINISTRATION",
        id: 466680043,
        title: "Hygiene Service Level",
        options: [
          {
            name: "Fixed facility observed (sink/tap) In dwelling",
            title: "Basic",
            color: "#753780",
          },
          {
            name: "Fixed facility observed (sink/tap)  In yard/plot",
            title: "Basic",
            color: "#753780",
          },
          {
            name: "Mobile object observed (bucket/jug/kettle)",
            title: "Limited",
            color: "#FDF177",
          },
          {
            name: "No handwashing place in dwelling/yard/plot",
            title: "No Facility",
            color: "#F1AC2A",
          },
          {
            name: "No permission to see",
            title: "No Facility",
            color: "#F1AC2A",
          },
        ],
      },
    ],
  },
  {
    id: 533560002,
    title: "Health Facilities",
    type: 1,
    map: {
      marker: {
        id: 547720005,
        title: "Health Center Facility Level",
        options: [
          {
            id: 1158,
            name: "L1",
          },
          {
            id: 1159,
            name: "L2",
          },
        ],
      },
      shape: {
        id: 555370007,
        title: "Number of usable toilets",
      },
    },
    charts: [
      {
        type: "ADMINISTRATION",
        id: 551560004,
        title: "Sanitation Service Level",
        options: [
          {
            name: "Yes",
            title: "Basic",
            color: "#67B769",
          },
          {
            name: "No, there are handwashing facilities near the toilets but lacking soap and/or water",
            title: "Limited",
            color: "#FCF176",
          },
          {
            name: "No, no handwashing facilities near toilets (within 5 meters)",
            title: "No Facility",
            color: "#F9CA29",
          },
        ],
      },
      {
        type: "ADMINISTRATION",
        id: 551560004,
        title: "Hygiene Service Level",
        options: [
          {
            name: "Yes",
            title: "Basic",
            color: "#753780",
          },
          {
            name: "No, there are handwashing facilities near the toilets but lacking soap and/or water",
            title: "Limited",
            color: "#FDF177",
          },
          {
            name: "No, no handwashing facilities near toilets (within 5 meters)",
            title: "No Facility",
            color: "#F1AC2A",
          },
        ],
      },
    ],
  },
  {
    id: 974754029,
    title: "CLTS",
    type: 1,
    map: {
      marker: {
        id: 557700349,
        title: "Open Defecation Status",
        options: [
          {
            id: 890,
            name: "Open Defecation",
          },
          {
            id: 891,
            name: "Triggered",
          },
          {
            id: 892,
            name: "Declared ODF",
          },
          {
            id: 893,
            name: "Verified ODF",
          },
        ],
      },
      shape: {
        id: 567440335,
        title: "Number of households in the Village",
      },
    },
    charts: [],
  },
  {
    id: 563350033,
    title: "WASH in School",
    type: 2,
    map: {
      marker: {
        id: 551660011,
        title: "Main source of drinking water",
      },
      shape: {
        id: 551660016,
        title: "No. of drinking water points",
      },
    },
    charts: [
      {
        type: "ADMINISTRATION",
        id: 551660011,
        title: "Water service level",
        options: [
          {
            name: "Piped water supply",
            title: "Basic",
            color: "#753780",
          },
          {
            name: "Protected well/spring",
            title: "Basic",
            color: "#753780",
          },
          {
            name: "Rainwater",
            title: "Limited",
            color: "#FDF177",
          },
          {
            name: "Unprotected well/spring",
            title: "No Services",
            color: "#F1AC2A",
          },
          {
            name: "Packaged bottled water",
            title: "Limited",
            color: "#FDF177",
          },
          {
            name: "Tanker-truck or cart",
            title: "Limited",
            color: "#FDF177",
          },
          {
            name: "Surface water (lake, river, stream)",
            title: "No Services",
            color: "#F1AC2A",
          },
          {
            name: "No water source",
            title: "No Services",
            color: "#F1AC2A",
          },
        ],
      },
      {
        type: "ADMINISTRATION",
        id: 551660029,
        title: "Sanitation Service Level",
        options: [
          {
            name: "Flush / Pour-flush toilets",
            title: "Basic",
            color: "#753780",
          },
          {
            name: "Pit latrines with slab",
            title: "Basic",
            color: "#753780",
          },
          {
            name: "Composting toilets",
            title: "Limited",
            color: "#FDF177",
          },
          {
            name: "Pit latrines without slab",
            title: "No Service",
            color: "#F1AC2A",
          },
          {
            name: "Hanging latrines",
            title: "No Service",
            color: "#F1AC2A",
          },
          {
            name: "Bucket latrines",
            title: "No Service",
            color: "#F1AC2A",
          },
          {
            name: "No toilets or latrines",
            title: "No Service",
            color: "#F1AC2A",
          },
        ],
      },
      {
        type: "ADMINISTRATION",
        id: 539710048,
        title: "Hygiene Service Level",
        options: [
          {
            name: "Yes, water and soap",
            title: "Basic",
            color: "#753780",
          },
          {
            name: "Water only",
            title: "Limited",
            color: "#FDF177",
          },
          {
            name: "Soap only",
            title: "Limited",
            color: "#FDF177",
          },
          {
            name: "Neither water or soap",
            title: "No Service",
            color: "#F1AC2A",
          },
        ],
      },
    ],
  },
  {
    id: 571070071,
    title: "Water System",
    type: 2,
    map: {
      marker: {
        id: 571050096,
        title: "Water Source Type",
      },
      shape: {
        id: 555960249,
        title: "Number of functional taps",
      },
    },
    charts: [
      {
        type: "PIE",
        id: 557710145,
        title: "Water System installed by",
      },
      {
        type: "BAR",
        id: 569070152,
        title: "Abstraction/Pump Equipment",
      },
      {
        type: "BAR",
        id: 571060083,
        title: "Source of Energy",
      },
      {
        type: "BAR",
        id: 571050096,
        title: "Water Source Type",
      },
    ],
  },
];

var highlights = [
  {
    name: "Sanitation",
    description:
      "proportion of population with access to hand washing facilities with water and soap",
    charts: [
      {
        // api chart/overview
        form_id: 519630048,
        type: "PIE",
        id: 513690066,
        title:
          "Does your sanitation facility leak or overflow wastes at any time of year?",
      },
      {
        // api chart/overview
        form_id: 563350033,
        type: "BARSTACK",
        id: 553480031, // support option / multiple_option / number
        title:
          "In your opinion, what should the school do to promote good hygiene and sanitation of students?",
        stack: {
          id: 553480033, // support option / multiple_option
          title:
            "Are there garbage or waste materials that are currently affecting the sanitation of the school?",
        },
      },
      {
        // api chart/overview/criteria
        form_id: 519630048,
        type: "CRITERIA",
        title: "Sanitation Service Level",
        options: [
          {
            name: "Safely Managed",
            color: "#368541",
            score: 15,
            options: [
              {
                question: 492490054,
                option: [
                  "Flush / pour flush",
                  "Pit latrine with slab",
                  "Twin pit with slab",
                ],
              },
              {
                question: 513690062,
                option: ["No"],
              },
              {
                question: 513690060,
                option: [
                  "Removed by service provider to a treatment plant",
                  "Removed by service provider to buried pit",
                  "Emptied by household buried in a covered pit",
                ],
              },
            ],
          },
          {
            name: "Basic",
            score: 10,
            color: "#79BE7D",
            options: [
              {
                question: 492490054,
                option: [
                  "Flush / pour flush",
                  "Pit latrine with slab",
                  "Twin pit with slab",
                ],
              },
              {
                question: 513690062,
                option: ["No"],
              },
            ],
          },
          {
            name: "Limited",
            score: -1,
            color: "#FDF177",
            options: [
              {
                question: 492490054,
                option: [
                  "Flush / pour flush",
                  "Pit latrine with slab",
                  "Twin pit with slab",
                ],
              },
              {
                question: 513690062,
                option: ["Yes"],
              },
            ],
          },
          {
            name: "Unimproved",
            score: -2,
            color: "#FBD256",
            options: [
              {
                question: 492490054,
                option: [
                  "Pit latrine without slab / Open pit",
                  "Twin pit without slab",
                  "Bucket",
                  "Hanging toilet / hanging latrine",
                ],
              },
            ],
          },
          {
            name: "Open Defecation",
            score: -3,
            color: "#F1AC2A",
            options: [
              {
                question: 492490054,
                option: ["No facility / Bush / Field"],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    name: "Hygiene",
    description: "Hygiene Text Description",
  },
  {
    name: "Waste Water",
    description: "Waste Water Text Description",
  },
  {
    name: "Water Quality",
    description: "Water Quality Text Description",
  },
  {
    name: "Efficiency",
    description: "Efficiency Text Description",
  },
  {
    name: "Water Stress",
    description: "Water Stress Text Description",
  },
  {
    name: "Ecosystems",
    description: "Ecosystems Text Description",
  },
];
