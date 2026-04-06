## Summary
- What changed?
- Which service(s) are affected? (`agent-assistant`, `agent-analytics`, or shared repo logic)
- Why is this needed?

## Validation
- [ ] `ruff check services/`
- [ ] `pytest services/*/tests -q`
- [ ] Docker build validated for affected service(s)
- [ ] Screenshots / output attached if relevant

## Release impact
- [ ] Safe for `dev`
- [ ] Candidate for `qa`
- [ ] Needs `preprod` validation
- [ ] Requires production approval

## Docs and changelog
- [ ] README / docs updated if behavior changed
- [ ] Release notes entry considered
