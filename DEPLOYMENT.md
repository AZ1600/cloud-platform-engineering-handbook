# Deploying This Handbook on Vercel

This handbook is a **static documentation website** built with VitePress. VitePress converts the Markdown files into HTML, CSS and JavaScript. Vercel then hosts those generated files and gives the handbook a public web address.

## The deployment flow

```text
Markdown chapters and project notes
             ↓
       VitePress build
             ↓
   Static website in .vitepress/dist
             ↓
        Vercel hosting
             ↓
  Public handbook URL and preview URLs
```

The source Markdown remains in GitHub. The generated `.vitepress/dist` directory is a build result, so it is ignored by Git and recreated during every deployment.

## Before deploying

You need:

- a GitHub repository containing this handbook;
- a Vercel account connected to GitHub; and
- the latest handbook changes committed and pushed to GitHub.

The repository should contain `package.json`, `package-lock.json`, `vercel.json`, `.vitepress/`, `index.md`, the numbered chapter directories and `projects/`.

## Check the website locally

Install the exact dependency versions recorded in `package-lock.json`:

```bash
npm ci
```

Start the development website:

```bash
npm run docs:dev
```

Open the local address printed in the terminal. Changes to Markdown normally appear automatically while this command is running.

Create the same production build that Vercel will create:

```bash
npm run docs:build
```

Preview that production build locally:

```bash
npm run docs:preview
```

If `npm run docs:build` fails, fix the reported Markdown, configuration or broken-link error before deploying.

## First deployment from the Vercel dashboard

1. Push the handbook repository to GitHub.
2. Sign in to Vercel and choose **Add New → Project**.
3. Import `AZ1600/cloud-platform-engineering-handbook`.
4. Leave the root directory as the repository root.
5. Confirm the build command is `npm run docs:build`.
6. Confirm the output directory is `.vitepress/dist`.
7. Select **Deploy**.

The checked-in `vercel.json` already records the build and output settings, so Vercel should detect them without manual changes.

## What happens after the first deployment

When changes are pushed to the production branch, Vercel rebuilds and republishes the production website. Work pushed through another branch or pull request can receive a separate preview deployment, allowing the content and layout to be checked before it becomes public.

The normal update cycle is:

```bash
git status
git add <files-you-reviewed>
git commit -m "docs: update engineering handbook"
git push
```

Always read `git status` and review the files before committing. Do not commit `node_modules`, `.vitepress/dist`, `.vitepress/cache` or `.vercel`; they are already listed in `.gitignore`.

## Custom domain

The default Vercel address is enough to publish the handbook. A custom domain can be added later from **Project Settings → Domains**. The domain should point to the handbook deployment, not to the GitHub repository itself.

## Important distinction

- **GitHub stores the source and history.**
- **VitePress turns the Markdown into a website.**
- **Vercel builds and hosts the website.**

That separation is useful: the handbook remains readable as Markdown in GitHub, while Vercel provides the polished reading experience.

## Troubleshooting

### Vercel cannot find the output

Confirm that the output directory is exactly:

```text
.vitepress/dist
```

### A page works locally but returns 404 online

Check the filename, capitalisation and link path. Production hosting is stricter about case differences than some local file systems.

### A page is missing from navigation

The Markdown page may exist but still need to be added to the navigation or sidebar in `.vitepress/config.mts`.

### The deployment uses old content

Confirm that the change was committed and pushed to the branch Vercel treats as the production branch. Local, uncommitted files are never sent to Vercel.

## Deployment checklist

- [ ] `npm ci` completes.
- [ ] `npm run docs:build` completes.
- [ ] The home page, a chapter, a project page and search work locally.
- [ ] `git status` contains only intentional changes.
- [ ] The changes are committed and pushed.
- [ ] The Vercel deployment finishes successfully.
- [ ] The public URL is checked on desktop and mobile.
