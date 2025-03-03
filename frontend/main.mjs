import { create } from "domain";
import { app, BrowserWindow, inAppPurchase } from "electron";
import { dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
let win;

function createWindow() {
    win = new BrowserWindow({
        width: 1440,
        height: 1024,
        webPreferences: {
            nodeIntegration: true,
            preload: `${__dirname}/preload.js`,
        },
    });

    win.loadURL("http://localhost:5173");
}

app.whenReady().then(() => {
    createWindow();

    app.on("activate", () => {
        if (BrowserWindow.getAllWindows().length == 0) {
            createWindow();
        }
    });
});

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
        app.quit();
    }
});