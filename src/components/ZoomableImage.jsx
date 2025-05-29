import Lightbox from "yet-another-react-lightbox";
import Zoom from "yet-another-react-lightbox/plugins/zoom";
import "yet-another-react-lightbox/styles.css";
import { useState, useEffect } from "react";

// 이미지 클릭 시 확대 가능하게 해주는 컴포넌트
export default function ZoomableImage({ src, width = "60%" }) {
  const [open, setOpen] = useState(false);

  // ESC 누르면 닫기
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") setOpen(false);
    };
    document.addEventListener("keydown", handleKeyDown);
    return () => document.removeEventListener("keydown", handleKeyDown);
  }, []);

  return (
    <div style={{ textAlign: "center" }}>
      {/* 썸네일 이미지 */}
      <img
        src={src}
        alt=""
        style={{ cursor: "zoom-in", width }}
        onClick={() => setOpen(true)}
      />

      {/* 팝업 이미지 + 커스텀 배경 클릭 닫기 레이어 */}
      {open && (
        <div
          onClick={() => setOpen(false)} // ✅ 배경 클릭 시 닫기
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            zIndex: 999,
            width: "100vw",
            height: "100vh",
            backgroundColor: "rgba(0, 0, 0, 0.9)",
          }}
        >
          <Lightbox
            open={open}
            close={() => setOpen(false)}
            slides={[{ src }]}
            plugins={[Zoom]}
            zoom={{
              maxZoomPixelRatio: 3,
              scrollToZoom: true,
              doubleClickToZoom: true,
              pinchToZoom: true
            }}
            animation={{ zoom: 300 }}
            styles={{
              navigationPrev: { display: "none" },
              navigationNext: { display: "none" },
              // 버튼은 보이게 할 수도 있음
            }}
          />
        </div>
      )}
    </div>
  );
}
