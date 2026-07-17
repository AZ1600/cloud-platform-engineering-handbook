# Handbook Writing Guide

This guide keeps every chapter practical, detailed, and connected to real engineering work.

## The Explanation Pattern

Every important topic should be explained in this order:

1. **Simple explanation** — describe the idea without assuming specialist knowledge.
2. **Problem it solves** — explain why the technology or pattern exists.
3. **Technical explanation** — introduce the correct engineering terminology and mechanics.
4. **How it works** — walk through the flow one step at a time.
5. **Project connection** — show exactly where the idea appears in PlatformPilot, CloudOps, Terraform EKS, the portfolio, or a future project.
6. **Engineering decision** — explain why this approach was chosen and what alternatives existed.
7. **Practical example** — include commands, configuration, code, a diagram, or a lab where useful.
8. **Production considerations** — cover security, reliability, observability, cost, scale, and operations.
9. **Common mistakes** — explain failure modes and how to diagnose them.
10. **Interview explanation** — provide a short answer and deeper follow-up points.
11. **Key takeaways** — finish with the few ideas the reader should remember.

## Project-First Rule

Concepts should not remain isolated theory. When a project uses a concept, the chapter should answer four questions:

- Where is it used?
- Why is it needed there?
- How was it implemented?
- What was learned from using it?

If a project does not yet implement the concept, label the section as a proposed improvement rather than describing it as completed work.

## Required “How I Used It” Block

Whenever a chapter introduces a technology that appears in my portfolio, include a block with these fields:

```text
Project:
Problem solved:
Where it appears:
Request or data flow:
Why I chose it:
Security responsibility:
Failure modes:
How I would verify it:
What I would improve:
Evidence level:
```

This block must be specific. “Used Kubernetes for deployment” is not enough. It should identify the workload, Kubernetes resources, image source, network path, identity, health signals, and deployment method.

## Example: Explaining Docker Through PlatformPilot

### Simple explanation

Docker packages an application with the runtime and dependencies it needs so that it can run consistently in different environments.

### Project problem

PlatformPilot has a React frontend and a FastAPI backend. Running them directly requires the correct Node.js, Python, and dependency versions on each machine.

### Project application

Each component can be built as a separate image. This preserves the boundary between the frontend and backend and creates deployment units suitable for Kubernetes.

### Decision to explain

The case study should record whether the team chose separate images, which base images were used, how image size and security were considered, and how configuration is provided at runtime.

### Production questions

- Are images built reproducibly and scanned?
- Does each container run as a non-root user?
- Are health checks defined?
- Are secrets injected rather than copied into the image?
- Are image tags immutable and traceable to a release?

This pattern turns a definition into evidence of engineering understanding.

## Chapter Quality Checklist

- [ ] The opening explains why the topic matters.
- [ ] Simple and technical explanations are both present.
- [ ] New terms are defined before being used heavily.
- [ ] The flow is broken into understandable steps.
- [ ] At least one real project connection is included.
- [ ] Current implementation and future plans are clearly separated.
- [ ] Important decisions and trade-offs are explained.
- [ ] Security, reliability, observability, and cost are considered where relevant.
- [ ] Common mistakes include diagnosis and resolution.
- [ ] Commands and examples have context and expected outcomes.
- [ ] Interview questions test understanding rather than memorisation.
- [ ] Claims are supported by project evidence.
- [ ] The summary reinforces the main ideas without introducing new material.

## Definition of Complete

A chapter is complete only when it is understandable to a learner, technically accurate, connected to at least one real project where applicable, and supported by evidence. Length alone does not make a chapter complete.
