# Withheld — implemented visual system

User-directed redesign, October 1, 2026. Reference: Unseen Studio through Mobbin. Original interface and code; no copied studio assets.

## Thesis
A calm, editorial working surface where unknown values stay visible. Large mixed sans/italic serif type introduces the idea; a live search in the first viewport begins the task. A sampled dataset changes from an unpublished/published dot field to a distribution of supported estimates. This animation explains provenance rather than implying recovered truth.

## Tokens
Paper #f4efeb; blush ground #eee5e1; plum ink #402c38; secondary plum #715c66; hairline #d2c2c8; estimate teal #28606b. Published values use plum, estimates use teal plus the explicit ≈ prefix and a range. Insufficient evidence is text, never a fabricated number. Source chips encode origin independently of color.

Instrument Serif regular/italic supplies display accents and the wordmark. Inter supplies readable UI and tabular figures. JetBrains Mono is limited to measurement/provenance labels. Fonts are self-hosted from Fontsource.

## Layout
Desktop asymmetric introduction and dataset sample; school workspace has a program list and a wider evidence detail column. Mobile stacks these and bounds the program list height. Compare uses at most three columns. Methodology uses metric rows, baseline bars, tables, an explicit processing sequence and a limits section.

## Motion and interaction
A single 1.1-second eased canvas transition explains the reveal. Rapid repeated clicks retarget from the current state. Reduced motion immediately switches states. Controls use 150–180ms color/opacity/transform feedback; no scroll hijack. Native inputs, selects, buttons and details preserve keyboard semantics. Visible focus, skip link and responsive content wrapping are implemented.

## Verification
Desktop 1440px and mobile 375px browser inspections caught/fixed heading and select overflow. Automated tests cover the real search→inspect→compare→export journey and failed-load retry. Exact evidence and screenshots are recorded in submission/gallery. This file describes the shipped world, superseding the old green-bar-printout planning contract.
