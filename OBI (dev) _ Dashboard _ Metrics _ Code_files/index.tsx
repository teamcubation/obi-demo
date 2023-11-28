import __vite__cjsImport0_react_jsxDevRuntime from "/node_modules/.vite/deps/react_jsx-dev-runtime.js?v=4650ddb1"; const jsxDEV = __vite__cjsImport0_react_jsxDevRuntime["jsxDEV"];
import { BrowserRouter } from "/node_modules/.vite/deps/react-router-dom.js?v=4650ddb1";
import { Provider } from "/node_modules/.vite/deps/react-redux.js?v=4650ddb1";
import App from "/src/App.tsx";
import store from "/src/store/index.ts";
import "/src/assets/scss/style.scss";
import config from "/src/config.ts";
import __vite__cjsImport7_reactDom_client from "/node_modules/.vite/deps/react-dom_client.js?v=4650ddb1"; const createRoot = __vite__cjsImport7_reactDom_client["createRoot"];
import __vite__cjsImport8_toastifyJs from "/node_modules/.vite/deps/toastify-js.js?v=4650ddb1"; const Toastify = __vite__cjsImport8_toastifyJs.__esModule ? __vite__cjsImport8_toastifyJs.default : __vite__cjsImport8_toastifyJs;
import "/node_modules/toastify-js/src/toastify.css";
import { registerSW } from "/@vite-plugin-pwa/virtual:pwa-register";
const container = document.getElementById("root");
const root = createRoot(container);
const updateSW = registerSW({
  onNeedRefresh() {
    Toastify({
      text: `<div><h4 style="display: inline">A new version is available!</h4></div>
                   <div style="margin-top: 5px;"><a class="do-sw-update">Click to update and reload</a></div>`,
      escapeMarkup: false,
      gravity: "bottom",
      duration: -1,
      className: "sw-update",
      onClick() {
        updateSW(true);
      }
    }).showToast();
  },
  onOfflineReady() {
  }
});
root.render(/* @__PURE__ */ jsxDEV(Provider, { store, children: /* @__PURE__ */ jsxDEV(BrowserRouter, { basename: config.basename, children: /* @__PURE__ */ jsxDEV(App, {}, void 0, false, {
  fileName: "/app/src/index.tsx",
  lineNumber: 42,
  columnNumber: 13
}, this) }, void 0, false, {
  fileName: "/app/src/index.tsx",
  lineNumber: 41,
  columnNumber: 9
}, this) }, void 0, false, {
  fileName: "/app/src/index.tsx",
  lineNumber: 40,
  columnNumber: 13
}, this));

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJtYXBwaW5ncyI6IkFBMENZO0FBekNaLFNBQVNBLHFCQUFxQjtBQUM5QixTQUFTQyxnQkFBZ0I7QUFHekIsT0FBT0MsU0FBUztBQUNoQixPQUFPQyxXQUFXO0FBR2xCLE9BQU87QUFDUCxPQUFPQyxZQUFZO0FBQ25CLFNBQVNDLGtCQUFrQjtBQUMzQixPQUFPQyxjQUFjO0FBQ3JCLE9BQU87QUFFUCxTQUFTQyxrQkFBa0I7QUFJM0IsTUFBTUMsWUFBWUMsU0FBU0MsZUFBZSxNQUFNO0FBQ2hELE1BQU1DLE9BQU9OLFdBQVdHLFNBQVU7QUFDbEMsTUFBTUksV0FBV0wsV0FBVztBQUFBLEVBQ3hCTSxnQkFBZ0I7QUFDWlAsYUFBUztBQUFBLE1BQ0xRLE1BQU87QUFBQTtBQUFBLE1BRVBDLGNBQWM7QUFBQSxNQUNkQyxTQUFTO0FBQUEsTUFDVEMsVUFBVTtBQUFBLE1BQ1ZDLFdBQVc7QUFBQSxNQUNYQyxVQUFVO0FBQ05QLGlCQUFTLElBQUk7QUFBQSxNQUNqQjtBQUFBLElBQ0osQ0FBQyxFQUFFUSxVQUFVO0FBQUEsRUFDakI7QUFBQSxFQUNBQyxpQkFBaUI7QUFBQSxFQUNiO0FBRVIsQ0FBQztBQUNEVixLQUFLVyxPQUNELHVCQUFDLFlBQVMsT0FDTixpQ0FBQyxpQkFBYyxVQUFVbEIsT0FBT21CLFVBQzVCLGlDQUFDLFNBQUQ7QUFBQTtBQUFBO0FBQUE7QUFBQSxPQUFJLEtBRFI7QUFBQTtBQUFBO0FBQUE7QUFBQSxPQUVBLEtBSEo7QUFBQTtBQUFBO0FBQUE7QUFBQSxPQUlBLENBQ0oiLCJuYW1lcyI6WyJCcm93c2VyUm91dGVyIiwiUHJvdmlkZXIiLCJBcHAiLCJzdG9yZSIsImNvbmZpZyIsImNyZWF0ZVJvb3QiLCJUb2FzdGlmeSIsInJlZ2lzdGVyU1ciLCJjb250YWluZXIiLCJkb2N1bWVudCIsImdldEVsZW1lbnRCeUlkIiwicm9vdCIsInVwZGF0ZVNXIiwib25OZWVkUmVmcmVzaCIsInRleHQiLCJlc2NhcGVNYXJrdXAiLCJncmF2aXR5IiwiZHVyYXRpb24iLCJjbGFzc05hbWUiLCJvbkNsaWNrIiwic2hvd1RvYXN0Iiwib25PZmZsaW5lUmVhZHkiLCJyZW5kZXIiLCJiYXNlbmFtZSJdLCJzb3VyY2VzIjpbImluZGV4LnRzeCJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyB0aGlyZCBwYXJ0eVxyXG5pbXBvcnQgeyBCcm93c2VyUm91dGVyIH0gZnJvbSAncmVhY3Qtcm91dGVyLWRvbSc7XHJcbmltcG9ydCB7IFByb3ZpZGVyIH0gZnJvbSAncmVhY3QtcmVkdXgnO1xyXG5cclxuLy8gcHJvamVjdCBpbXBvcnRzXHJcbmltcG9ydCBBcHAgZnJvbSAnQXBwJztcclxuaW1wb3J0IHN0b3JlIGZyb20gJ3N0b3JlJztcclxuXHJcbi8vIHN0eWxlICsgYXNzZXRzXHJcbmltcG9ydCAnYXNzZXRzL3Njc3Mvc3R5bGUuc2Nzcyc7XHJcbmltcG9ydCBjb25maWcgZnJvbSAnY29uZmlnJztcclxuaW1wb3J0IHsgY3JlYXRlUm9vdCB9IGZyb20gJ3JlYWN0LWRvbS9jbGllbnQnO1xyXG5pbXBvcnQgVG9hc3RpZnkgZnJvbSAndG9hc3RpZnktanMnO1xyXG5pbXBvcnQgJ3RvYXN0aWZ5LWpzL3NyYy90b2FzdGlmeS5jc3MnO1xyXG4vLyBAdHMtaWdub3JlXHJcbmltcG9ydCB7IHJlZ2lzdGVyU1cgfSBmcm9tICd2aXJ0dWFsOnB3YS1yZWdpc3Rlcic7XHJcblxyXG4vLyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT18fCBSRUFDVCBET00gUkVOREVSICB8fD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSAvL1xyXG5cclxuY29uc3QgY29udGFpbmVyID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3Jvb3QnKTtcclxuY29uc3Qgcm9vdCA9IGNyZWF0ZVJvb3QoY29udGFpbmVyISk7XHJcbmNvbnN0IHVwZGF0ZVNXID0gcmVnaXN0ZXJTVyh7XHJcbiAgICBvbk5lZWRSZWZyZXNoKCkge1xyXG4gICAgICAgIFRvYXN0aWZ5KHtcclxuICAgICAgICAgICAgdGV4dDogYDxkaXY+PGg0IHN0eWxlPVwiZGlzcGxheTogaW5saW5lXCI+QSBuZXcgdmVyc2lvbiBpcyBhdmFpbGFibGUhPC9oND48L2Rpdj5cclxuICAgICAgICAgICAgICAgICAgIDxkaXYgc3R5bGU9XCJtYXJnaW4tdG9wOiA1cHg7XCI+PGEgY2xhc3M9XCJkby1zdy11cGRhdGVcIj5DbGljayB0byB1cGRhdGUgYW5kIHJlbG9hZDwvYT48L2Rpdj5gLFxyXG4gICAgICAgICAgICBlc2NhcGVNYXJrdXA6IGZhbHNlLFxyXG4gICAgICAgICAgICBncmF2aXR5OiAnYm90dG9tJyxcclxuICAgICAgICAgICAgZHVyYXRpb246IC0xLFxyXG4gICAgICAgICAgICBjbGFzc05hbWU6ICdzdy11cGRhdGUnLFxyXG4gICAgICAgICAgICBvbkNsaWNrKCkge1xyXG4gICAgICAgICAgICAgICAgdXBkYXRlU1codHJ1ZSk7XHJcbiAgICAgICAgICAgIH1cclxuICAgICAgICB9KS5zaG93VG9hc3QoKTtcclxuICAgIH0sXHJcbiAgICBvbk9mZmxpbmVSZWFkeSgpIHtcclxuICAgICAgICAvLyBzaG93IGEgcmVhZHkgdG8gd29yayBvZmZsaW5lIHRvIHVzZXJcclxuICAgIH1cclxufSk7XHJcbnJvb3QucmVuZGVyKFxyXG4gICAgPFByb3ZpZGVyIHN0b3JlPXtzdG9yZX0+XHJcbiAgICAgICAgPEJyb3dzZXJSb3V0ZXIgYmFzZW5hbWU9e2NvbmZpZy5iYXNlbmFtZX0+XHJcbiAgICAgICAgICAgIDxBcHAgLz5cclxuICAgICAgICA8L0Jyb3dzZXJSb3V0ZXI+XHJcbiAgICA8L1Byb3ZpZGVyPlxyXG4pO1xyXG4iXSwiZmlsZSI6Ii9hcHAvc3JjL2luZGV4LnRzeCJ9