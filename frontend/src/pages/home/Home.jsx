import React, { useState, useEffect } from "react";
import "./style.scss";
import { Tabs } from "antd";
import {
  HomeDataChart,
  HomeAdministrationChart,
  HomeMap,
} from "../../components";
import { queue } from "../../lib";
const { TabPane } = Tabs;

export const Visuals = ({ current }) => {
  return (
    <div>
      <div className="map-wrapper">
        {current?.maps && (
          <HomeMap
            markerData={{ features: [] }}
            style={{ height: 600 }}
            current={current}
          />
        )}
      </div>
      <div className="chart-wrapper">
        {current?.charts?.map((hc, hcI) =>
          hc.type === "ADMINISTRATION" || hc.type === "CRITERIA" ? (
            <HomeAdministrationChart
              key={`chart-${hc.id}-${hcI}`}
              formId={hc.form_id}
              config={hc}
              index={hcI + 1}
              identifier={current?.name}
            />
          ) : (
            <HomeDataChart
              key={`chart-${hc.form_id}-${hcI}`}
              formId={hc.form_id}
              config={hc}
              index={hcI + 1}
            />
          )
        )}
      </div>
    </div>
  );
};

const Home = () => {
  const { highlights } = window;
  const [currentHighlight, setCurrentHighlight] = useState(highlights?.[0]);

  const onTabClick = (active) => {
    setCurrentHighlight(highlights.find((x) => x.name === active));
    queue.update((q) => {
      q.next = 1;
    });
  };

  useEffect(() => {
    queue.update((q) => {
      q.next = 1;
    });
  }, []);

  return (
    <div id="home">
      <div className="home-odd about">
        <h1>About RUSH</h1>
        <p>
          The Kenya Rural Urban Sanitation and Hygiene (RUSH) platform is a
          real-time monitoring and information system owned by the Ministry of
          Health. The platform aggregates quantitative and qualitative data from
          county and national levels and facilitates data analysis, report
          generation and visualizations.
        </p>
      </div>
      <div className="home-even highlights">
        <div className="body">
          <Tabs
            defaultActiveKey={highlights?.[0]?.name}
            onTabClick={onTabClick}
            centered
          >
            {highlights?.map((highlight) => (
              <TabPane tab={highlight.name} key={highlight.name}>
                <p className="highlight-title">{highlight.description}</p>
              </TabPane>
            ))}
          </Tabs>
          <Visuals current={currentHighlight} />
        </div>
      </div>
    </div>
  );
};

export default React.memo(Home);
