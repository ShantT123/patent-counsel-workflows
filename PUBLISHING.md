# Publishing this preview on GitHub

1. Extract `patent-counsel-workflows-v0.1.0.zip` on your computer.
2. On GitHub, create a public repository named `patent-counsel-workflows` under your own account. Suggested description: "Open-source AI workflows for patent counsel: invention intake, source-linked disclosures, and filing-review preparation."
3. In the new repository, choose the option to upload existing files. Upload the **contents** of the extracted `patent-counsel-workflows` folder, including its subfolders. The README should appear at the repository root. If the browser omits `.gitignore`, add it separately or use GitHub Desktop.
4. Review the file list and commit the files. The included MIT LICENSE should be the repository license; do not add a conflicting second license.
5. Optionally create a GitHub release tagged `v0.1.0`, labeled as a pre-release. Describe it as an invention-intake preview with synthetic examples and an unexecuted behavioral evaluation set.

Uploading only the ZIP as a repository file will not make the README and skill browsable. The ZIP can be an optional release attachment after the source files are uploaded.

## Before announcing it

- Review the public author credit: Shant Tchakerian.
- Read the skill and worked example and make any changes you want to own professionally.
- Confirm MIT is the license you want; it permits reuse, modification, and commercial use subject to its terms.
- Run a fresh-session demonstration and have its output reviewed before making performance claims. The current example is manually prepared.
- Add a professional profile link or bio only if you want one. None has been invented in this package.

## Suggested first feedback request

Ask a patent practitioner to run the synthetic example and identify the three most consequential omissions or incorrect inferences. Record the model, date, and skill version. Use the evaluation rubric to turn that feedback into reproducible improvements.
