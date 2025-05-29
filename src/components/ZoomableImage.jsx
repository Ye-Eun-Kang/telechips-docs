import Lightbox from "yet-another-react-lightbox";
import Zoom from "yet-another-react-lightbox/plugins/zoom";
import "yet-another-react-lightbox/styles.css";
import { useState } from "react";

// 이미지 클릭 시 확대 가능하게 해주는 컴포넌트
export default function ZoomableImage({ src, width = "60%" }) {
  const [open, setOpen] = useState(false);

  return (
    // 이미지 전체를 감싸는 영역을 가운데 정렬
    <div style={{ textAlign: "center" }}>
      {/* 클릭 가능한 썸네일 이미지 */}
      <img
        src={src}
        alt=""
        style={{ cursor: "zoom-in", width }}
        onClick={() => setOpen(true)}
      />
      {/* 팝업 확대 이미지 */}
      <Lightbox
        open={open}
        close={() => setOpen(false)}
        slides={[{ src }]}
        plugins={[Zoom]}
        zoom={{
          maxZoomPixelRatio: 3,     // 확대 비율 제한
          scrollToZoom: true        // 마우스 휠 확대 허용
        }}
        animation={{ zoom: 300 }}
        styles={{
          navigationPrev: { display: "none" },
          navigationNext: { display: "none" },
          button: { display: "none" },
        }}
      />
    </div>
  );
}
