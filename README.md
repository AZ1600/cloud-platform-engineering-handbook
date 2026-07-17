# 📘 Cloud & Platform Engineering Handbook

> A project-led handbook documenting how I apply Cloud Engineering, Platform Engineering, Kubernetes, AWS, DevOps, AI Operations, and modern software engineering.

---

## 👋 Welcome

This repository serves as my personal engineering handbook and the technical record of the projects I build.

Rather than collecting scattered notes, I document concepts, architectures, commands, interview preparation, and lessons learned from real-world projects.

The goal is to build a comprehensive knowledge base that grows throughout my career. Each concept should connect to a project, an engineering decision, a practical lab, or a lesson learned.

Topics are explained in simple language first, followed by technical details, real project examples, interview questions, best practices, and useful commands.

## How to Use This Handbook

There are two useful reading paths:

1. **Learn by topic:** start with the foundation chapters, then move into platform engineering and operations.
2. **Learn by project:** open the [Project Index](projects/README.md), choose a project, and follow its links back to the concepts used to build it.

The project path is the heart of this handbook. It shows not only what I know, but where I applied it, why I made particular decisions, and what I learned.

All new chapters follow the [Handbook Writing Guide](HANDBOOK-WRITING-GUIDE.md): simple explanation first, technical depth second, then project application, decisions, production considerations, troubleshooting, and interview preparation.

The [Technology-to-Project Evidence Map](TECHNOLOGY-PROJECT-MAP.md) shows exactly where each technology appears in my projects, what it does there, and what I must understand before claiming it as a skill.

The [Project and Work Register](PROJECT-WORK-REGISTER.md) records every owned repository reviewed for this handbook. The [Project Command Reference](13-Command-Reference/Chapter-13-Commands.md) collects verified setup, build, test, deployment, validation and troubleshooting commands with explanations and safety notes.

The handbook is also a VitePress website. Use the [Vercel Deployment Guide](DEPLOYMENT.md) to understand how the Markdown becomes a public site, how to test it locally, and which settings Vercel needs.

The [Debugging and Issue Register](DEBUGGING-ISSUE-REGISTER.md) records what failed, how it was investigated, what solved it, and how recurrence can be prevented. It separates verified fixes, reported fixes, review findings, and simulated failures so every project explanation remains honest.

---

# 📚 Table of Contents

## 📖 Volume I – Foundations

- [Chapter 1 – Cloud Computing Fundamentals](01-Cloud-Fundamentals/Chapter-01-Cloud-Computing.md)
- [Chapter 2 – Linux Fundamentals](02-Linux/Chapter-02-Linux.md)
- [Chapter 3 – Docker Fundamentals](03-Docker/Chapter-03-Docker.md)
- [Chapter 4 – Kubernetes Through My Projects](04-Kubernetes/Chapter-04-Kubernetes.md)
- [Chapter 5 – AWS Through My Projects](05-AWS/Chapter-05-AWS.md)

---

## ⚙️ Volume II – Platform Engineering

- [Chapter 6 – Platform Engineering](06-Platform-Engineering/Chapter-06-Platform-Engineering.md)
- [Chapter 7 – Infrastructure as Code (Terraform)](07-Terraform/Chapter-07-Terraform.md)
- [Chapter 8 – CI/CD & GitOps](08-CICD/Chapter-08-CICD.md)
- [Chapter 9 – Observability](09-Observability/Chapter-09-Observability.md)
- [Chapter 10 – AI Operations](10-AI-Operations/Chapter-10-AI-Operations.md)

---

## 🏗️ Volume III – Project & Architecture Case Studies

- [Project Index](projects/README.md)
- [PlatformPilot](projects/PlatformPilot.md)
- [CloudOps Command Center](projects/CloudOps-Command-Center.md)
- [Terraform AWS EKS Platform](projects/Terraform-AWS-EKS-Platform.md)
- [Pharmacy API on Amazon EKS](projects/Pharmacy-API-EKS.md)
- [GitOps with Argo CD](projects/GitOps-ArgoCD.md)
- [Backstage Developer Portal](projects/Backstage-Developer-Portal.md)
- [OpsPilot SaaS](projects/OpsPilot-SaaS.md)
- [AI-Powered Content Automation Platform](projects/AI-Content-Automation-Platform.md)
- [AI Resume Analyzer with Bedrock and n8n](projects/AI-Resume-Analyzer.md)
- [Cloud-Native Pharmacy Platform](projects/Cloud-Native-Pharmacy-Platform.md)
- [Platform Engineering CI/CD Pipeline](projects/CI-CD-Pipeline.md)
- [Platform Engineering Observability](projects/Observability-Platform.md)
- [Cloud Control Plane — Flagship Vision](projects/Cloud-Control-Plane.md)

---

## 💼 Volume IV – Interview Preparation

- [Chapter 11 – Architecture Through My Projects](11-Architecture/Chapter-11-Architecture.md)
- [Chapter 12 – Interview Preparation From My Projects](12-Interview-Preparation/Chapter-12-Interview-Preparation.md)

---

## 💻 Volume V – Command Reference

- [Commands Used Across My Projects](13-Command-Reference/Chapter-13-Commands.md)
- Git and repository commands
- Python, Node.js and application commands
- Docker and Docker Compose commands
- Kubernetes and Argo CD commands
- Terraform and AWS SAM commands
- Testing, database and observability commands

---

## 📓 Volume VI – Lessons Learned

- [Chapter 14 – Lessons Learned Across My Projects](14-Lessons-Learned/Chapter-14-Lessons-Learned.md)
- [Debugging and Issue Register](DEBUGGING-ISSUE-REGISTER.md)

---

# 🎯 Purpose

This handbook helps me:

- Strengthen my understanding of Cloud and Platform Engineering
- Prepare for technical interviews
- Document project architectures
- Record lessons learned
- Build a long-term engineering reference

---

# 🚀 Technologies Covered

- AWS
- Kubernetes
- Docker
- Terraform
- FastAPI
- React
- Python
- GitHub Actions
- Prometheus
- Grafana
- Linux
- Platform Engineering
- DevOps
- AI Operations

---

# 📈 Roadmap

- [x] Create topic chapters for Cloud, Linux, Docker, Kubernetes and AWS
- [x] Create Platform Engineering, Terraform, CI/CD, Observability and AI Operations chapters
- [x] Create Architecture, Interview Preparation, Command Reference and Lessons Learned chapters
- [x] Add project catalogue and documentation structure
- [x] Complete code-level PlatformPilot case study
- [x] Add initial case studies for all included engineering repositories
- [x] Add commands verified from repositories and executable configuration
- [ ] Deepen every non-PlatformPilot case study through full code-level review
- [ ] Add project screenshots and diagrams
- [ ] Add automated Markdown link and structure checks in CI
- [ ] Publish Version 1.0

---

## 👨‍💻 Author

**Olawale Azeez**

Cloud | Platform | DevOps Engineer

GitHub: https://github.com/AZ1600

---

## Documentation Standard

Every project is documented using the same structure: problem, users, architecture, technology choices, implementation, security, observability, delivery, trade-offs, incidents, lessons learned, interview talking points, and evidence. New projects should start from the [project case-study template](templates/project-case-study-template.md).
