import { defineConfig } from "vitepress";

const chapters = [
  { text: "1. Cloud Fundamentals", link: "/01-Cloud-Fundamentals/Chapter-01-Cloud-Computing" },
  { text: "2. Linux", link: "/02-Linux/Chapter-02-Linux" },
  { text: "3. Docker", link: "/03-Docker/Chapter-03-Docker" },
  { text: "4. Kubernetes", link: "/04-Kubernetes/Chapter-04-Kubernetes" },
  { text: "5. AWS", link: "/05-AWS/Chapter-05-AWS" },
  { text: "6. Platform Engineering", link: "/06-Platform-Engineering/Chapter-06-Platform-Engineering" },
  { text: "7. Terraform", link: "/07-Terraform/Chapter-07-Terraform" },
  { text: "8. CI/CD and GitOps", link: "/08-CICD/Chapter-08-CICD" },
  { text: "9. Observability", link: "/09-Observability/Chapter-09-Observability" },
  { text: "10. AI Operations", link: "/10-AI-Operations/Chapter-10-AI-Operations" },
  { text: "11. Architecture", link: "/11-Architecture/Chapter-11-Architecture" },
  { text: "12. Interview Preparation", link: "/12-Interview-Preparation/Chapter-12-Interview-Preparation" },
  { text: "13. Command Reference", link: "/13-Command-Reference/Chapter-13-Commands" },
  { text: "14. Lessons Learned", link: "/14-Lessons-Learned/Chapter-14-Lessons-Learned" },
];

const projects = [
  { text: "Project Index", link: "/projects/" },
  { text: "PlatformPilot", link: "/projects/PlatformPilot" },
  { text: "CloudOps Command Center", link: "/projects/CloudOps-Command-Center" },
  { text: "OpsPilot SaaS", link: "/projects/OpsPilot-SaaS" },
  { text: "Pharmacy API on EKS", link: "/projects/Pharmacy-API-EKS" },
  { text: "Cloud-Native Pharmacy", link: "/projects/Cloud-Native-Pharmacy-Platform" },
  { text: "Terraform AWS EKS", link: "/projects/Terraform-AWS-EKS-Platform" },
  { text: "GitOps with Argo CD", link: "/projects/GitOps-ArgoCD" },
  { text: "CI/CD Pipeline", link: "/projects/CI-CD-Pipeline" },
  { text: "Observability Platform", link: "/projects/Observability-Platform" },
  { text: "Backstage Portal", link: "/projects/Backstage-Developer-Portal" },
  { text: "AI Content Automation", link: "/projects/AI-Content-Automation-Platform" },
  { text: "AI Resume Analyzer", link: "/projects/AI-Resume-Analyzer" },
  { text: "Cloud Control Plane Vision", link: "/projects/Cloud-Control-Plane" },
];

export default defineConfig({
  title: "Cloud & Platform Engineering Handbook",
  description:
    "Olawale Azeez's project-led guide to cloud, Kubernetes, AWS, platform engineering, delivery, observability and AI operations.",
  lang: "en-GB",
  cleanUrls: true,
  lastUpdated: true,
  head: [
    ["meta", { name: "theme-color", content: "#0f766e" }],
    ["meta", { name: "author", content: "Olawale Azeez" }],
    ["meta", { property: "og:type", content: "website" }],
    ["meta", { property: "og:title", content: "Cloud & Platform Engineering Handbook" }],
    [
      "meta",
      {
        property: "og:description",
        content: "Concepts explained through real cloud and platform engineering projects.",
      },
    ],
  ],
  themeConfig: {
    siteTitle: "Engineering Handbook",
    logo: {
      light: "/logo-light.svg",
      dark: "/logo-dark.svg",
      alt: "Cloud and Platform Engineering Handbook",
    },
    nav: [
      { text: "Home", link: "/" },
      { text: "Learn", items: chapters.slice(0, 10) },
      { text: "Projects", link: "/projects/" },
      { text: "Commands", link: "/13-Command-Reference/Chapter-13-Commands" },
      { text: "Interview", link: "/12-Interview-Preparation/Chapter-12-Interview-Preparation" },
    ],
    sidebar: [
      {
        text: "Start Here",
        items: [
          { text: "Handbook Home", link: "/" },
          { text: "How to Use the Handbook", link: "/README" },
          { text: "Deploy on Vercel", link: "/DEPLOYMENT" },
          { text: "Debugging and Issue Register", link: "/DEBUGGING-ISSUE-REGISTER" },
          { text: "Technology-to-Project Map", link: "/TECHNOLOGY-PROJECT-MAP" },
          { text: "Project and Work Register", link: "/PROJECT-WORK-REGISTER" },
        ],
      },
      {
        text: "Learning Chapters",
        collapsed: false,
        items: chapters,
      },
      {
        text: "Project Case Studies",
        collapsed: true,
        items: projects,
      },
    ],
    search: {
      provider: "local",
      options: {
        detailedView: true,
      },
    },
    outline: {
      level: [2, 3],
      label: "On this page",
    },
    socialLinks: [
      { icon: "github", link: "https://github.com/AZ1600" },
    ],
    editLink: {
      pattern:
        "https://github.com/AZ1600/cloud-platform-engineering-handbook/edit/main/:path",
      text: "Edit this page on GitHub",
    },
    lastUpdated: {
      text: "Last updated",
      formatOptions: {
        dateStyle: "medium",
        timeStyle: "short",
      },
    },
    docFooter: {
      prev: "Previous topic",
      next: "Next topic",
    },
    footer: {
      message: "Built from verified projects, decisions, commands and lessons.",
      copyright: "© 2026 Olawale Azeez",
    },
  },
});
