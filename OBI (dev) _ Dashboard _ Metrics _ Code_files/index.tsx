import __vite__cjsImport0_react_jsxDevRuntime from "/node_modules/.vite/deps/react_jsx-dev-runtime.js?v=20751ed2"; const jsxDEV = __vite__cjsImport0_react_jsxDevRuntime["jsxDEV"];
import { BrowserRouter } from "/node_modules/.vite/deps/react-router-dom.js?v=20751ed2";
import { Provider } from "/node_modules/.vite/deps/react-redux.js?v=20751ed2";
import App from "/src/App.tsx";
import store from "/src/store/index.ts";
import "/src/assets/scss/style.scss";
import config from "/src/config.ts";
import __vite__cjsImport7_reactDom_client from "/node_modules/.vite/deps/react-dom_client.js?v=20751ed2"; const createRoot = __vite__cjsImport7_reactDom_client["createRoot"];
import __vite__cjsImport8_toastifyJs from "/node_modules/.vite/deps/toastify-js.js?v=20751ed2"; const Toastify = __vite__cjsImport8_toastifyJs.__esModule ? __vite__cjsImport8_toastifyJs.default : __vite__cjsImport8_toastifyJs;
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
  lineNumber: 41,
  columnNumber: 13
}, this) }, void 0, false, {
  fileName: "/app/src/index.tsx",
  lineNumber: 40,
  columnNumber: 9
}, this) }, void 0, false, {
  fileName: "/app/src/index.tsx",
  lineNumber: 39,
  columnNumber: 13
}, this));

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJtYXBwaW5ncyI6IkFBeUNZO0FBeENaLFNBQVNBLHFCQUFxQjtBQUM5QixTQUFTQyxnQkFBZ0I7QUFHekIsT0FBT0MsU0FBUztBQUNoQixPQUFPQyxXQUFXO0FBR2xCLE9BQU87QUFDUCxPQUFPQyxZQUFZO0FBQ25CLFNBQVNDLGtCQUFrQjtBQUMzQixPQUFPQyxjQUFjO0FBQ3JCLE9BQU87QUFFUCxTQUFTQyxrQkFBa0I7QUFJM0IsTUFBTUMsWUFBWUMsU0FBU0MsZUFBZSxNQUFNO0FBQ2hELE1BQU1DLE9BQU9OLFdBQVdHLFNBQVU7QUFDbEMsTUFBTUksV0FBV0wsV0FBVztBQUFBLEVBQ3hCTSxnQkFBZ0I7QUFDWlAsYUFBUztBQUFBLE1BQ0xRLE1BQU87QUFBQTtBQUFBLE1BRVBDLGNBQWM7QUFBQSxNQUNkQyxTQUFTO0FBQUEsTUFDVEMsVUFBVTtBQUFBLE1BQ1ZDLFVBQVU7QUFDTk4saUJBQVMsSUFBSTtBQUFBLE1BQ2pCO0FBQUEsSUFDSixDQUFDLEVBQUVPLFVBQVU7QUFBQSxFQUNqQjtBQUFBLEVBQ0FDLGlCQUFpQjtBQUFBLEVBQ2I7QUFFUixDQUFDO0FBQ0RULEtBQUtVLE9BQ0QsdUJBQUMsWUFBUyxPQUNOLGlDQUFDLGlCQUFjLFVBQVVqQixPQUFPa0IsVUFDNUIsaUNBQUMsU0FBRDtBQUFBO0FBQUE7QUFBQTtBQUFBLE9BQUksS0FEUjtBQUFBO0FBQUE7QUFBQTtBQUFBLE9BRUEsS0FISjtBQUFBO0FBQUE7QUFBQTtBQUFBLE9BSUEsQ0FDSiIsIm5hbWVzIjpbIkJyb3dzZXJSb3V0ZXIiLCJQcm92aWRlciIsIkFwcCIsInN0b3JlIiwiY29uZmlnIiwiY3JlYXRlUm9vdCIsIlRvYXN0aWZ5IiwicmVnaXN0ZXJTVyIsImNvbnRhaW5lciIsImRvY3VtZW50IiwiZ2V0RWxlbWVudEJ5SWQiLCJyb290IiwidXBkYXRlU1ciLCJvbk5lZWRSZWZyZXNoIiwidGV4dCIsImVzY2FwZU1hcmt1cCIsImdyYXZpdHkiLCJkdXJhdGlvbiIsIm9uQ2xpY2siLCJzaG93VG9hc3QiLCJvbk9mZmxpbmVSZWFkeSIsInJlbmRlciIsImJhc2VuYW1lIl0sInNvdXJjZXMiOlsiaW5kZXgudHN4Il0sInNvdXJjZXNDb250ZW50IjpbIi8vIHRoaXJkIHBhcnR5XHJcbmltcG9ydCB7IEJyb3dzZXJSb3V0ZXIgfSBmcm9tICdyZWFjdC1yb3V0ZXItZG9tJztcclxuaW1wb3J0IHsgUHJvdmlkZXIgfSBmcm9tICdyZWFjdC1yZWR1eCc7XHJcblxyXG4vLyBwcm9qZWN0IGltcG9ydHNcclxuaW1wb3J0IEFwcCBmcm9tICdBcHAnO1xyXG5pbXBvcnQgc3RvcmUgZnJvbSAnc3RvcmUnO1xyXG5cclxuLy8gc3R5bGUgKyBhc3NldHNcclxuaW1wb3J0ICdhc3NldHMvc2Nzcy9zdHlsZS5zY3NzJztcclxuaW1wb3J0IGNvbmZpZyBmcm9tICdjb25maWcnO1xyXG5pbXBvcnQgeyBjcmVhdGVSb290IH0gZnJvbSAncmVhY3QtZG9tL2NsaWVudCc7XHJcbmltcG9ydCBUb2FzdGlmeSBmcm9tICd0b2FzdGlmeS1qcyc7XHJcbmltcG9ydCAndG9hc3RpZnktanMvc3JjL3RvYXN0aWZ5LmNzcyc7XHJcbi8vIEB0cy1pZ25vcmVcclxuaW1wb3J0IHsgcmVnaXN0ZXJTVyB9IGZyb20gJ3ZpcnR1YWw6cHdhLXJlZ2lzdGVyJztcclxuXHJcbi8vID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXx8IFJFQUNUIERPTSBSRU5ERVIgIHx8PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IC8vXHJcblxyXG5jb25zdCBjb250YWluZXIgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgncm9vdCcpO1xyXG5jb25zdCByb290ID0gY3JlYXRlUm9vdChjb250YWluZXIhKTtcclxuY29uc3QgdXBkYXRlU1cgPSByZWdpc3RlclNXKHtcclxuICAgIG9uTmVlZFJlZnJlc2goKSB7XHJcbiAgICAgICAgVG9hc3RpZnkoe1xyXG4gICAgICAgICAgICB0ZXh0OiBgPGRpdj48aDQgc3R5bGU9XCJkaXNwbGF5OiBpbmxpbmVcIj5BIG5ldyB2ZXJzaW9uIGlzIGF2YWlsYWJsZSE8L2g0PjwvZGl2PlxyXG4gICAgICAgICAgICAgICAgICAgPGRpdiBzdHlsZT1cIm1hcmdpbi10b3A6IDVweDtcIj48YSBjbGFzcz1cImRvLXN3LXVwZGF0ZVwiPkNsaWNrIHRvIHVwZGF0ZSBhbmQgcmVsb2FkPC9hPjwvZGl2PmAsXHJcbiAgICAgICAgICAgIGVzY2FwZU1hcmt1cDogZmFsc2UsXHJcbiAgICAgICAgICAgIGdyYXZpdHk6ICdib3R0b20nLFxyXG4gICAgICAgICAgICBkdXJhdGlvbjogLTEsXHJcbiAgICAgICAgICAgIG9uQ2xpY2soKSB7XHJcbiAgICAgICAgICAgICAgICB1cGRhdGVTVyh0cnVlKTtcclxuICAgICAgICAgICAgfVxyXG4gICAgICAgIH0pLnNob3dUb2FzdCgpO1xyXG4gICAgfSxcclxuICAgIG9uT2ZmbGluZVJlYWR5KCkge1xyXG4gICAgICAgIC8vIHNob3cgYSByZWFkeSB0byB3b3JrIG9mZmxpbmUgdG8gdXNlclxyXG4gICAgfVxyXG59KTtcclxucm9vdC5yZW5kZXIoXHJcbiAgICA8UHJvdmlkZXIgc3RvcmU9e3N0b3JlfT5cclxuICAgICAgICA8QnJvd3NlclJvdXRlciBiYXNlbmFtZT17Y29uZmlnLmJhc2VuYW1lfT5cclxuICAgICAgICAgICAgPEFwcCAvPlxyXG4gICAgICAgIDwvQnJvd3NlclJvdXRlcj5cclxuICAgIDwvUHJvdmlkZXI+XHJcbik7XHJcbiJdLCJmaWxlIjoiL2FwcC9zcmMvaW5kZXgudHN4In0=