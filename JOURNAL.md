# Module 3 Journal

## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues — selected issue: `BiasDetector` regex patterns miss several documented bias cases, causing 9 unit test failures in `tests/unit/test_bias_detector.py`.

**Issue title:** BiasDetector regex patterns are too narrow — 9 unit tests fail due to unmatched bias phrase variants

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**
The `BiasDetector` class in `safety/bias_detector.py` is responsible for flagging biased language in AI-generated portfolio feedback. Its `DISMISSIVE_PATTERNS` and `DEMOGRAPHIC_PATTERNS` regex lists are too narrowly written: they match only specific phrase structures while missing natural variations of the same sentiment (e.g., "bootcamp graduates can't write code" is not caught, but "bootcamp education is inadequate" is). This causes 9 of 32 unit tests to fail. A successful fix expands the pattern lists to cover the documented variants tested in `tests/unit/test_bias_detector.py` without introducing false positives for neutral or positive language.

**Branch name:** fix/bias-detector-pattern-gaps

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [ ] Issue added to cohort ledger

---

### Is This Issue Right for Me? — Checklist Notes

- **Part 1 — Understanding the Issue:** I can explain it without re-reading: `BiasDetector.detect_bias()` returns `(False, "")` for inputs like "bootcamp graduates can't write production code" when it should return `(True, reason)`. The gap is between the regex patterns and the natural language variants the tests cover.
- **Part 2 — Tier Fit:** Tier 1 — the fix lives entirely in one file (`safety/bias_detector.py`), requires no understanding of the broader system, and involves only regex pattern expansion.
- **Part 3 — Codebase Readiness:** I located the specific patterns and corresponding test file before beginning. I read every test end-to-end and verified which phrases were not matched.
- **Part 4 — Scope and Time:** No blockers or dependencies. Estimated 1–2 hours of focused work, entirely achievable in Week 7.
