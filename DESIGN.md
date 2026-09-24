# DESIGN: Withheld

> **Status:** design intent, written before the build (Thu Sep 24 2026). impeccable's flow has the finished DESIGN.md re-documented *from the built world* at finish; this file will be replaced by that pass, and the tokens below are the starting contract. The direction contract lives in `.impeccable/surfaces/index-html.md`.

## World: the green-bar printout

The Scorecard's numbers come out of federal batch systems (NSLDS loan records matched to IRS earnings). Withheld renders them as the object that world used to print on: **continuous-feed green-bar paper**. The machine prints what it's allowed to print. Where the record is withheld, it prints `PrivacySuppressed` and nothing else. Estimates are **annotations in non-photo-blue pencil**, the draftsman's colour that by definition isn't part of the reproduced record. That's exactly what an estimate is.

**Provenance is encoded by medium, before value:**

| What | Medium | Never |
|---|---|---|
| Official published figure | line-printer ink (`--ink`), mono, no prefix | never pencil blue |
| Withheld | the literal machine word `PrivacySuppressed`, ink at 55 % | never a blank cell or a "—" |
| Model estimate | pencil blue (`--pencil`), prefixed `≈`, always followed by its interval `[low – high]` | never without its interval; never bare |
| The federal earnings line | one red rule (`--rule-red`) with its dollar value | red is reserved for the line |

**Physical scene:** a student and a parent at a kitchen table in the evening, laptop and phone, a financial-aid letter nearby. A paper document read under house light, so the world is **light**, and `color-scheme: light` is declared. Dark-mode users still get a legible paper sheet rather than an inverted one.

**Refused (category defaults):** fintech cards with gauges, gradient area charts, green/red up-down semantics, glassmorphism, hero illustration, cream + serif + terracotta, near-black + neon.

## Colour (Restrained strategy: paper neutrals + two functional inks + one red rule)

| Token | Value | Use | Contrast |
|---|---|---|---|
| `--paper` | `#FBFCF8` | page ground (cool white, not cream) | n/a |
| `--band` | `#E4EFDF` | green-bar bands (3 print lines tall) | n/a (ground) |
| `--band-edge` | `#B9D1B4` | band edges, sprocket holes, hairlines | non-text |
| `--ink` | `#17202A` | official figures, headings, body | 15.97:1 on paper, 13.87:1 on band |
| `--ink-2` | `#46525E` | secondary text, report headers | 7.75:1 on paper, 6.74:1 on band |
| `--ink-faint` | `#5C6671` | `PrivacySuppressed`, axis labels | 5.67:1 on paper, 4.93:1 on band |
| `--pencil` | `#1A6AA0` | estimate text and interval brackets | 5.64:1 on paper, 4.90:1 on band |
| `--pencil-wash` | `#A9D8EE` | non-photo-blue fills, interval bars, hatching | non-text |
| `--rule-red` | `#B8262B` | the federal earnings line and its label only | 6.08:1 on paper, 5.29:1 on band |
| `--focus` | `#1A6AA0` + 2 px offset | focus ring | matches pencil |

Colour is never the only encoding. Above/below the line is also position (ticks above or below the rule) and words ("likely above", "too close to call", "likely below"). Estimates are also marked by `≈` and brackets.

## Type

| Role | Face | Why |
|---|---|---|
| Prose, UI labels | **Public Sans** (variable, 400–700) | The U.S. government's own typeface (U.S. Web Design System). The data's native voice, and a workhorse at small sizes |
| Figures, tables, report headers | **Martian Mono** (variable, width 75–112.5, weights 300–700) | Line-printer register; the width axis condenses columns on phones instead of truncating |
| The few giant numerals | **Doto** (dot-matrix, 700–900) | A dot-matrix printer's numeral, used for at most one figure per viewport |

Contrast ratios computed with the WCAG 2.x relative-luminance formula (script in `scripts/contrast.py` once the build lands).

Scale (rem, 16 px root): 0.75 · 0.875 · 1 · 1.125 · 1.375 · 1.75 · 2.5 · 4 · clamp(4.5rem, 12vw, 9.5rem) for Doto. The mono line is `1.5rem` (24 px), and everything in the printout snaps to it. A band is 3 lines = 72 px.

## Layout grammar
- **The sheet:** a max-width 1440 px continuous sheet with sprocket-hole margins (16 px wide, holes every 24 px) on desktop. On phones the margins drop, and the sheet becomes a 40-column "narrow carriage" printout.
- **Report header** at the top of every section, like a batch report: `RUN 2026-09-24 · SOURCE Most-Recent-Cohorts-Field-of-Study · SHA-256 3f1a… · PAGE 0003`. These carry real values from the pipeline, never decoration.
- **Tear rule** (perforation: a dashed line of small circles) between major sections instead of cards and borders.
- **Tables are native.** Right-aligned tabular figures, column headers in mono caps, row heights on the 24 px line.
- One spacing rhythm: 8 px base; section spacing 72 px (one band) or 144 px.

## Motion (decided with emil's animate process: purpose → properties → curve → interruption)
- **Line-printer feed** (hero field only): published ticks print in bands top to bottom in ~900 ms, `steps()`-quantised to feel mechanical. Purpose: shows the record exists before the blanks become the point.
- **The pencil pass** (the signature): withheld ticks are pencilled in left → right in ~1.6 s, `cubic-bezier(0.2, 0.8, 0.2, 1)`. Replayable from a control. Interruptible: scrolling away or pressing Esc completes it instantly.
- **Tear-off:** a looked-up program's row lifts out of the printout into its statement (transform + opacity, 240 ms, ease-out); the exit is 160 ms.
- Hover/press: 120 ms colour and translate only. No layout-shifting properties.
- `prefers-reduced-motion: reduce`: no feed, no pencil sweep, no tear-off. Final states render immediately.

## Components (initial list)
Program lookup (combobox, keyboard-first) · program statement (the verdict, published vs estimate, interval bar vs red rule, debt → payment → D/E) · the field (canvas, 233,979 ticks, progressive load) · validation report (tables + one calibration chart per `dataviz`) · method notes · footer with "Built by Rishik Rontala".
