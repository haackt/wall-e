# Details

Date : 2023-02-03 11:13:25

Directory /Users/haack/Developer/wall-e

Total : 61 files,  8133 codes, 65 comments, 362 blanks, all 8560 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [README.md](/README.md) | Markdown | 93 | 0 | 57 | 150 |
| [arduino/Wall_E.cpp](/arduino/Wall_E.cpp) | C++ | 185 | 30 | 23 | 238 |
| [client/index.html](/client/index.html) | HTML | 17 | 0 | 1 | 18 |
| [client/package-lock.json](/client/package-lock.json) | JSON | 5,877 | 0 | 1 | 5,878 |
| [client/package.json](/client/package.json) | JSON | 34 | 0 | 1 | 35 |
| [client/postcss.config.cjs](/client/postcss.config.cjs) | JavaScript | 9 | 2 | 3 | 14 |
| [client/public/favicon.svg](/client/public/favicon.svg) | XML | 11 | 0 | 0 | 11 |
| [client/public/logo.svg](/client/public/logo.svg) | XML | 18 | 0 | 0 | 18 |
| [client/src/App.svelte](/client/src/App.svelte) | Svelte | 20 | 0 | 6 | 26 |
| [client/src/app.postcss](/client/src/app.postcss) | PostCSS | 17 | 0 | 4 | 21 |
| [client/src/lib/components/Dashboard.svelte](/client/src/lib/components/Dashboard.svelte) | Svelte | 177 | 0 | 19 | 196 |
| [client/src/lib/components/Dashboard/DashboardButton.svelte](/client/src/lib/components/Dashboard/DashboardButton.svelte) | Svelte | 9 | 0 | 2 | 11 |
| [client/src/lib/components/Dashboard/Joystick.svelte](/client/src/lib/components/Dashboard/Joystick.svelte) | Svelte | 184 | 0 | 44 | 228 |
| [client/src/lib/components/Dialogs/ConnectDialog.svelte](/client/src/lib/components/Dialogs/ConnectDialog.svelte) | Svelte | 183 | 0 | 16 | 199 |
| [client/src/lib/components/Dialogs/ConnectDialog/BackButton.svelte](/client/src/lib/components/Dialogs/ConnectDialog/BackButton.svelte) | Svelte | 6 | 0 | 2 | 8 |
| [client/src/lib/components/Dialogs/ConnectDialog/ConnectStepContainer.svelte](/client/src/lib/components/Dialogs/ConnectDialog/ConnectStepContainer.svelte) | Svelte | 4 | 0 | 1 | 5 |
| [client/src/lib/components/Dialogs/ConnectDialog/ContinueButton.svelte](/client/src/lib/components/Dialogs/ConnectDialog/ContinueButton.svelte) | Svelte | 7 | 0 | 2 | 9 |
| [client/src/lib/components/Dialogs/DialogContainer.svelte](/client/src/lib/components/Dialogs/DialogContainer.svelte) | Svelte | 37 | 0 | 5 | 42 |
| [client/src/lib/components/Dialogs/MenuDialog.svelte](/client/src/lib/components/Dialogs/MenuDialog.svelte) | Svelte | 80 | 0 | 4 | 84 |
| [client/src/lib/components/Dialogs/ServoDialog.svelte](/client/src/lib/components/Dialogs/ServoDialog.svelte) | Svelte | 109 | 0 | 8 | 117 |
| [client/src/lib/components/Dialogs/SpeakDialog.svelte](/client/src/lib/components/Dialogs/SpeakDialog.svelte) | Svelte | 58 | 0 | 6 | 64 |
| [client/src/lib/components/Dialogs/SpeakDialogButton.svelte](/client/src/lib/components/Dialogs/SpeakDialogButton.svelte) | Svelte | 9 | 0 | 2 | 11 |
| [client/src/lib/components/Gamepad/SwitchControlMethodButton.svelte](/client/src/lib/components/Gamepad/SwitchControlMethodButton.svelte) | Svelte | 14 | 0 | 3 | 17 |
| [client/src/lib/components/Icons/arrows-up-down.svelte](/client/src/lib/components/Icons/arrows-up-down.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/bars-3.svelte](/client/src/lib/components/Icons/bars-3.svelte) | Svelte | 14 | 0 | 2 | 16 |
| [client/src/lib/components/Icons/cog.svelte](/client/src/lib/components/Icons/cog.svelte) | Svelte | 53 | 0 | 2 | 55 |
| [client/src/lib/components/Icons/cpu-chip.svelte](/client/src/lib/components/Icons/cpu-chip.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/film.svelte](/client/src/lib/components/Icons/film.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/finger-print.svelte](/client/src/lib/components/Icons/finger-print.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/hand-raised.svelte](/client/src/lib/components/Icons/hand-raised.svelte) | Svelte | 19 | 0 | 2 | 21 |
| [client/src/lib/components/Icons/language.svelte](/client/src/lib/components/Icons/language.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/laser.svelte](/client/src/lib/components/Icons/laser.svelte) | Svelte | 21 | 0 | 2 | 23 |
| [client/src/lib/components/Icons/microphone.svelte](/client/src/lib/components/Icons/microphone.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/paper-plane.svelte](/client/src/lib/components/Icons/paper-plane.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/speaker.svelte](/client/src/lib/components/Icons/speaker.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/square-plus.svelte](/client/src/lib/components/Icons/square-plus.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/star.svelte](/client/src/lib/components/Icons/star.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/thumbs-up.svelte](/client/src/lib/components/Icons/thumbs-up.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Icons/x-circle.svelte](/client/src/lib/components/Icons/x-circle.svelte) | Svelte | 18 | 0 | 2 | 20 |
| [client/src/lib/components/Stepper/Stepper.svelte](/client/src/lib/components/Stepper/Stepper.svelte) | Svelte | 46 | 0 | 3 | 49 |
| [client/src/lib/components/Stepper/StepperIcon.svelte](/client/src/lib/components/Stepper/StepperIcon.svelte) | Svelte | 20 | 0 | 2 | 22 |
| [client/src/lib/components/Stepper/StepperText.svelte](/client/src/lib/components/Stepper/StepperText.svelte) | Svelte | 12 | 0 | 2 | 14 |
| [client/src/lib/layout/Footer.svelte](/client/src/lib/layout/Footer.svelte) | Svelte | 3 | 0 | 1 | 4 |
| [client/src/lib/layout/Header.svelte](/client/src/lib/layout/Header.svelte) | Svelte | 19 | 0 | 4 | 23 |
| [client/src/lib/toast.ts](/client/src/lib/toast.ts) | TypeScript | 3 | 1 | 1 | 5 |
| [client/src/main.ts](/client/src/main.ts) | TypeScript | 6 | 1 | 3 | 10 |
| [client/src/stores/gamepad.ts](/client/src/stores/gamepad.ts) | TypeScript | 3 | 0 | 2 | 5 |
| [client/src/stores/servo.ts](/client/src/stores/servo.ts) | TypeScript | 2 | 0 | 2 | 4 |
| [client/src/stores/websocket.ts](/client/src/stores/websocket.ts) | TypeScript | 4 | 0 | 2 | 6 |
| [client/src/vite-env.d.ts](/client/src/vite-env.d.ts) | TypeScript | 0 | 2 | 1 | 3 |
| [client/svelte.config.js](/client/svelte.config.js) | JavaScript | 10 | 2 | 2 | 14 |
| [client/tailwind.config.cjs](/client/tailwind.config.cjs) | JavaScript | 24 | 0 | 3 | 27 |
| [client/tsconfig.json](/client/tsconfig.json) | JSON with Comments | 14 | 6 | 1 | 21 |
| [client/tsconfig.node.json](/client/tsconfig.node.json) | JSON | 8 | 0 | 1 | 9 |
| [client/vite.config.ts](/client/vite.config.ts) | TypeScript | 37 | 1 | 2 | 40 |
| [server/camera.py](/server/camera.py) | Python | 29 | 2 | 7 | 38 |
| [server/commands.py](/server/commands.py) | Python | 26 | 3 | 21 | 50 |
| [server/requirements.txt](/server/requirements.txt) | pip requirements | 183 | 0 | 1 | 184 |
| [server/speaker.py](/server/speaker.py) | Python | 5 | 1 | 5 | 11 |
| [server/walle_app.py](/server/walle_app.py) | Python | 110 | 14 | 50 | 174 |
| [server/web/trust.html](/server/web/trust.html) | HTML | 88 | 0 | 4 | 92 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)