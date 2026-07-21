# Task Journal: #40 Accessibility: Use Native HTML5 Dialog

## Selection
- Selected item #40: [Agent Suggestion] Accessibility: Use Native HTML5 Dialog.

## Re-evaluation
- Confirmed valid. Modals using `div` with absolute positioning require a lot of manual focus trapping and keyboard event handling, whereas native HTML5 `<dialog>` handles this out-of-the-box.

## Next Steps
- Delegate to headless `agy` using `gemini-3.1-pro-high` to refactor `MethodologyModal.jsx` to use the native `<dialog>` element.
