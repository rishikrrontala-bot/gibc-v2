# Demo video: Withheld

Final running time: **3:44** (223.91 seconds). English synthetic narration with burned-in English captions; H.264 1920 × 1080 video. This is a recording of actual browser interactions with the shipped prototype. Narrator: Kokoro-82M via kokoro-onnx, stock `af_heart` voice, speed 0.94. This is not Rishik’s voice and does not imitate a real person. No music or third-party footage.

## Timed script

Rishik can record these same lines in his own voice if desired. The provided MP4 is already usable.

### 0:00–0:17 / Intro

Shot: Home page; click Reveal at 0:06.

Some numbers are withheld. Your questions shouldn't be. In this College Scorecard release, seventy point eight percent of program records suppress their five year earnings. Withheld makes that missing information visible, then shows what a model can cautiously estimate.

### 0:17–0:33 / Search

Shot: Select Rutgers.

This is a working research prototype built by Rishik Rontala for the Global Innovation Build Challenge. Search more than thirty five hundred colleges. Let's open Rutgers and explore an aerospace engineering program.

### 0:33–0:53 / Estimate

Shot: Show selected aerospace estimate and range.

The teal label matters: this is a model estimate, not an official outcome. The middle estimate is about ninety four thousand dollars, with a target eighty percent interval from roughly eighty eight to one hundred five thousand. The interval describes a program median, not an individual's salary.

### 0:53–1:12 / Evidence

Shot: Expand the evidence explanation.

Open the evidence explanation. The model uses public program attributes and comparable training programs. When there are fewer than thirty training peers in the same field and credential, Withheld declines to estimate. Other kinds of missing data stay unavailable.

### 1:12–1:31 / Loan

Shot: Enter $12,000 and 0%; show $100/month.

The calculator turns a hypothetical loan into monthly terms. Change the amount and rate, and the payment updates immediately. Twelve thousand dollars over ten years at zero interest is one hundred dollars a month. This is an illustration, not a borrowing recommendation.

### 1:31–1:47 / Published

Shot: Pin aerospace; filter Computer, Bachelor, Published.

Now add this program to a comparison, then find a published computer science outcome. Published observations keep a distinct label. The interface never quietly replaces an official value with a model prediction.

### 1:47–2:05 / Compare

Shot: Pin the published program, compare, export CSV.

Compare programs side by side while keeping their sources and uncertainty visible. An editable benchmark is only your reference, not a federal eligibility threshold. Export the comparison as a CSV with the source labels and release date intact.

### 2:05–2:25 / Metrics

Shot: Open The methodology and held-out results.

The methodology page shows the evidence behind the design. Institution families are separated into training, calibration and test groups. On eight thousand seven hundred twenty three held out published outcomes, the model's average absolute error is about nine thousand thirty dollars.

### 2:25–2:44 / Baselines

Shot: Show baseline chart and size-stratified coverage.

That improves on the field and credential median baseline. But the intervals cover only seventy seven point six percent of test outcomes against an eighty percent target. Coverage is lower for small programs. Both the improvement and the shortfall are reported.

### 2:44–3:05 / Pipeline

Shot: Show the source → separation → model → calibration steps.

Under the hood, three Light G B M quantile models learn from field, credential, state, institution type and completions. Separate calibration data expands their intervals. A frozen, reproducible pipeline exports the results, and the browser searches them without an account or a paid API.

### 3:05–3:27 / Limits

Shot: Show the limitations section.

The most important limitation is simple: we cannot test against outcomes the government has not published. Suppression is not random. Performance on published programs does not establish reliability on suppressed programs. These estimates do not recover private data or automate real money decisions.

### 3:27–3:43 / Close

Shot: Return to the home page.

Withheld brings the question, the evidence and the uncertainty into the same view. The source code, model files, data provenance and validation results are public. Explore the live prototype, inspect the work, and keep the gaps in sight.

## Production and reproduction

- `scenes.json` contains the narration; `timeline.json` contains measured audio durations; `captions.srt` contains English subtitles.
- `scripts/narrate.py` creates local narration with externally downloaded Kokoro ONNX weights. Weights are not part of the application. See https://github.com/thewh1teagle/kokoro-onnx and its model-files-v1.0 release. Kokoro model weights are Apache-2.0; the ONNX wrapper is MIT.
- `scripts/record-demo.mjs` drives Playwright and captures the real interface at 12 frames/second; FFmpeg outputs H.264. `scripts/finish-video.sh` burns the subtitles and muxes AAC narration normalized for consistent playback loudness.
- The application remains silent. Audio is only in the demonstration video.
- Upload `video/demo.mp4` to YouTube (unlisted is allowed), Vimeo or Youku. A private video or only a GitHub MP4 link does not meet the event requirement.
