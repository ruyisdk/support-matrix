# Welcome to Pull Request

Thank you for your contribution! Please refer to the [contributing guidelines](../CONTRIBUTING.md) for more details.

## If you are working on the support-matrix report

We appreciate your effort in improving the support matrix. To generate the SVG image locally, you can use:

```sh
python assets/generate_svgimage.py -p . -o assets/output --html https://${{ github.repository_owner }}.github.io/support-matrix
```

For internationalization (i18n) SVG generation  test, simply add the `-l zh` option.

If you're creating a new report, please refer to our templates:
- [Board report template](../report-template/[board-name]/README.md)
- [OS report template](../report-template/[board-name]/[os-name]/README.md)

### Checklist
- [ ] SVG table generation passes successfully
- [ ] Appropriate changes to documentation are included in the PR
- [ ] i18n for documentation (optional)

## If you are working on the assets toolchain

Fixes #<issue_number_goes_here>

> We recommend opening an issue for discussion before making significant changes.

### Checklist
- [ ] Changes to workflow/codes are fully tested
- [ ] Appropriate changes to documentation are included in the PR
- [ ] This fixes an issue
- [ ] New feature added
