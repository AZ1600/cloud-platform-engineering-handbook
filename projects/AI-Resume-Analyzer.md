# AI Resume Analyzer with AWS Bedrock and n8n

> An automated workflow that compares résumé skills with cloud and platform engineering role requirements and generates readiness analysis and development recommendations.

**Repository:** <https://github.com/AZ1600/ai-resume-analyzer-n8n>  
**Last verified:** 2026-07-11 against the repository README

## How It Works

```text
Resume data -> n8n -> skill extraction -> JavaScript scoring
            -> AWS Bedrock / Amazon Nova Pro -> recommendations
```

The deterministic scoring stage and generative analysis stage serve different purposes. JavaScript calculates structured readiness and gap information; the language model turns that context into explanations and recommendations.

## Verified Evidence

- Exported n8n workflow.
- AWS Bedrock and Amazon Nova Pro integration.
- Custom JavaScript scoring logic.
- Docker Compose environment.
- Screenshots of the workflow, execution, scoring, and output.

## Engineering Questions

- How are skill names normalised before comparison?
- How is scoring tested for consistency and bias?
- Does the prompt prevent unsupported claims about candidates?
- How are résumé data and model inputs protected?
- How is model output validated before display?
