# Chapter 1 — Cloud Computing Fundamentals

> Cloud computing allows individuals and organisations to access computing resources over the internet instead of purchasing, installing, and maintaining all the physical infrastructure themselves.

---

## Learning Objectives

By the end of this chapter, you should be able to:

- Explain cloud computing in simple and technical terms.
- Describe why cloud computing was created.
- Identify the main characteristics and benefits of cloud services.
- Differentiate between IaaS, PaaS, and SaaS.
- Explain public, private, hybrid, and multi-cloud environments.
- Understand scalability, elasticity, high availability, and fault tolerance.
- Explain disaster recovery concepts such as RTO and RPO.
- Describe the cloud shared responsibility model.
- Connect cloud concepts to practical engineering projects.
- Answer common cloud computing interview questions.

---

## 1. Introduction

Imagine that you have an idea for a new application.

Before the cloud, you might have needed to:

1. Purchase physical servers.
2. Find a secure place to store them.
3. Install operating systems and applications.
4. Configure networking equipment.
5. Provide electricity and cooling.
6. Replace failed hardware.
7. Hire engineers to maintain the environment.

This required a large financial investment before the application could serve its first customer.

It also created another problem: capacity planning.

If you purchased too little infrastructure, the application could fail when demand increased. If you purchased too much, expensive equipment could remain unused.

Cloud computing changed this model.

Instead of buying and maintaining every physical component, organisations can rent computing resources from providers such as:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)

Resources such as virtual servers, databases, storage, networking, analytics, and artificial intelligence services can be created in minutes.

This allows engineers to focus more on applications, automation, reliability, and customer needs instead of managing physical data centres.

Cloud computing now supports many areas of modern technology, including:

- Software development
- DevOps
- Platform Engineering
- Artificial intelligence
- Data analytics
- Internet of Things
- Cybersecurity
- Container orchestration
- Serverless computing
- Cloud-native applications

---

## 2. What Is Cloud Computing?

### Simple Explanation

Cloud computing is similar to renting a service instead of buying and maintaining all the equipment yourself.

Imagine that you need a powerful computer for one month.

Buying the computer would be expensive, especially if you no longer needed it after that month. A better option might be to rent the computing power and return it when the work is complete.

Cloud computing follows the same idea.

Organisations rent resources such as servers, storage, databases, and networking over the internet. They can create the resources when needed, change their size as demand changes, and remove them when they are no longer required.

---

### Technical Definition

Cloud computing is the on-demand delivery of computing capabilities over a network, usually the internet.

These capabilities may include:

- Compute
- Storage
- Networking
- Databases
- Analytics
- Security services
- Artificial intelligence
- Machine learning
- Monitoring
- Messaging
- Container platforms
- Serverless functions

Customers can provision resources without purchasing the underlying physical hardware.

They usually pay according to usage, subscription, reservation, or another consumption-based pricing model.

---

## 3. Traditional Infrastructure and Cloud Infrastructure

### Traditional Infrastructure

In a traditional environment, an organisation owns and manages most of the technology stack.

```text
Organisation
    │
    ▼
Purchase physical servers
    │
    ▼
Install servers in a data centre
    │
    ▼
Configure power, cooling, and networking
    │
    ▼
Install operating systems
    │
    ▼
Deploy applications
    │
    ▼
Maintain and replace hardware
```

The organisation is responsible for:

- Physical security
- Server hardware
- Storage devices
- Networking equipment
- Power and cooling
- Operating systems
- Software installation
- Monitoring
- Maintenance
- Capacity planning

---

### Cloud Infrastructure

With cloud computing, the provider manages the underlying facilities and hardware.

```text
Organisation
    │
    ▼
Choose a cloud service
    │
    ▼
Provision resources through a console, CLI, or API
    │
    ▼
Deploy the application
    │
    ▼
Monitor usage and adjust capacity
    │
    ▼
Pay according to the selected pricing model
```

The customer still has important responsibilities, but the cloud provider removes much of the physical infrastructure burden.

---

## 4. Why Cloud Computing Exists

Cloud computing developed in response to several limitations of traditional infrastructure.

### 4.1 High Upfront Cost

Physical servers, storage, networking equipment, data-centre space, electricity, and cooling can require a significant capital investment.

Cloud computing reduces this initial cost by allowing customers to rent resources.

---

### 4.2 Slow Provisioning

Purchasing, delivering, installing, and configuring physical infrastructure may take weeks or months.

A cloud resource can often be created within minutes.

---

### 4.3 Difficult Capacity Planning

It can be difficult to predict how much infrastructure an application will require.

An organisation may:

- Purchase too little and experience performance problems.
- Purchase too much and waste money on unused capacity.

Cloud resources can be resized or removed as requirements change.

---

### 4.4 Hardware Maintenance

Physical equipment can fail and eventually becomes outdated.

Cloud providers operate the underlying hardware and replace failed components as part of their service.

---

### 4.5 Global Expansion

Building data centres in multiple countries is expensive.

Cloud providers already operate infrastructure in many geographic locations, allowing organisations to deploy applications closer to their users.

---

### 4.6 Need for Faster Innovation

Development teams often need temporary environments for testing, experimentation, and feature development.

Cloud computing allows teams to create and remove environments quickly, supporting faster delivery.

---

## 5. Key Characteristics of Cloud Computing

Cloud computing is commonly described using five main characteristics.

---

### 5.1 On-Demand Self-Service

Customers can provision resources without waiting for a provider employee to perform the work manually.

For example, an engineer can launch an Amazon EC2 instance through:

- The AWS Management Console
- The AWS CLI
- An SDK
- Terraform
- CloudFormation
- An API request

This makes infrastructure available quickly.

---

### 5.2 Broad Network Access

Cloud services can be accessed over a network using standard mechanisms.

They may be accessed through:

- Web browsers
- Mobile devices
- Command-line tools
- APIs
- Software development kits
- Private network connections

Broad network access allows distributed teams and applications to use cloud resources from many locations.

---

### 5.3 Resource Pooling

Cloud providers maintain large pools of compute, storage, and networking resources.

These resources serve many customers while maintaining logical isolation between them.

This approach is known as multi-tenancy.

Customers normally do not control the exact physical server hosting their workloads, but they can choose logical locations such as regions and availability zones.

---

### 5.4 Rapid Elasticity

Resources can increase or decrease as demand changes.

For example:

```text
Normal traffic
    │
    ▼
Two application instances
    │
    ▼
Traffic increases
    │
    ▼
Auto Scaling adds more instances
    │
    ▼
Traffic decreases
    │
    ▼
Extra instances are removed
```

To users, cloud capacity may appear almost unlimited, although practical service quotas, costs, and regional capacity still apply.

---

### 5.5 Measured Service

Cloud providers measure resource consumption.

Usage may be calculated using:

- Compute time
- Number of requests
- Storage capacity
- Data transfer
- Database operations
- Active users
- Execution duration

This allows customers to monitor usage and understand costs.

---

## 6. Benefits of Cloud Computing

### 6.1 Reduced Upfront Cost

Organisations do not need to purchase all their infrastructure before starting a project.

Cloud services can convert some capital expenditure into operational expenditure.

---

### 6.2 Faster Provisioning

Engineers can create resources quickly.

This reduces the time required to:

- Build development environments
- Test ideas
- Deploy applications
- Recover from failures
- Expand infrastructure

---

### 6.3 Scalability

Cloud resources can support increasing workloads by adding capacity.

This may involve:

- Increasing the size of a resource.
- Adding more instances.
- Using managed scaling services.
- Distributing traffic across multiple systems.

---

### 6.4 Elasticity

Elastic systems can grow and shrink in response to demand.

This can reduce waste because resources do not have to remain at peak size permanently.

---

### 6.5 High Availability

Applications can be distributed across independent locations to reduce the risk of a single failure causing an outage.

---

### 6.6 Global Reach

Cloud providers operate infrastructure in multiple geographic regions.

Organisations can place applications closer to their users, reducing latency and supporting data-residency requirements.

---

### 6.7 Managed Services

Cloud providers offer managed databases, queues, monitoring systems, container platforms, and many other services.

Managed services reduce the amount of infrastructure that customers must operate themselves.

---

### 6.8 Automation

Cloud resources are controlled through APIs, which makes automation possible.

Infrastructure can be created using tools such as:

- Terraform
- AWS CloudFormation
- AWS SAM
- Pulumi
- Ansible
- CI/CD pipelines

---

### 6.9 Reliability and Recovery

Cloud platforms provide services for:

- Backups
- Replication
- Monitoring
- Automated replacement
- Disaster recovery
- Multi-region architectures

These capabilities can improve reliability when they are configured correctly.

---

## 7. Cloud Service Models

Cloud services are commonly divided into three major models:

- Infrastructure as a Service
- Platform as a Service
- Software as a Service

The main difference is how responsibility is divided between the provider and the customer.

---

### 7.1 Infrastructure as a Service — IaaS

IaaS provides fundamental computing resources such as:

- Virtual machines
- Storage
- Networking
- Load balancers
- Firewalls

The provider manages the physical data centre, networking equipment, storage hardware, and server hardware.

The customer usually manages:

- The operating system
- Installed software
- Applications
- Application data
- Security configuration
- Patching of customer-managed systems

Examples include:

- Amazon EC2
- Amazon EBS
- Amazon VPC
- Azure Virtual Machines
- Google Compute Engine

#### When IaaS Is Useful

IaaS is suitable when an organisation needs:

- Greater control over the operating system.
- Custom software configurations.
- Traditional applications.
- Flexible networking.
- Migration from physical or virtual data centres.

---

### 7.2 Platform as a Service — PaaS

PaaS provides an environment where developers can deploy applications without managing the underlying operating system and much of the runtime infrastructure.

The provider normally manages:

- Physical infrastructure
- Virtualisation
- Operating systems
- Runtime environments
- Some scaling and availability features

The customer focuses mainly on:

- Application code
- Application configuration
- Data
- Access control

Examples include:

- AWS Elastic Beanstalk
- Azure App Service
- Google App Engine
- Heroku

#### When PaaS Is Useful

PaaS is suitable when teams want to:

- Deploy applications quickly.
- Reduce infrastructure management.
- Use standard application runtimes.
- Focus primarily on software development.

---

### 7.3 Software as a Service — SaaS

SaaS provides a complete application managed by the provider.

Users normally access the application through a web browser, mobile application, or API.

The provider manages almost the entire technology stack.

Examples include:

- Gmail
- Microsoft 365
- Salesforce
- Slack
- Dropbox

#### When SaaS Is Useful

SaaS is suitable when an organisation needs a ready-to-use solution without building and operating the software internally.

---

### Responsibility Comparison

| Layer | IaaS | PaaS | SaaS |
|---|---|---|---|
| Application | Customer | Customer | Provider |
| Data configuration | Customer | Customer | Shared/Customer |
| Runtime | Customer | Provider | Provider |
| Operating system | Customer | Provider | Provider |
| Virtualisation | Provider | Provider | Provider |
| Servers | Provider | Provider | Provider |
| Storage hardware | Provider | Provider | Provider |
| Networking hardware | Provider | Provider | Provider |

The exact division of responsibility varies by provider and service.

---

## 8. Cloud Deployment Models

### 8.1 Public Cloud

A public cloud is operated by a third-party provider and serves multiple customers.

Examples include:

- AWS
- Microsoft Azure
- Google Cloud

Resources are logically isolated, even though customers may share underlying physical infrastructure.

#### Advantages

- Fast provisioning
- Wide service selection
- Global infrastructure
- Consumption-based pricing
- Reduced hardware management

---

### 8.2 Private Cloud

A private cloud is dedicated to one organisation.

It may run:

- Inside the organisation’s own data centre.
- In a dedicated hosted facility.
- On infrastructure managed by a third party.

Private clouds may provide greater control, but they usually require more operational effort.

---

### 8.3 Hybrid Cloud

A hybrid cloud combines private infrastructure with public cloud services.

For example:

```text
Private data centre
        │
        ├── Sensitive legacy systems
        │
        └── Internal databases
                 │
          Secure connection
                 │
                 ▼
            Public cloud
                 │
        ├── Web applications
        ├── Analytics
        └── Backup services
```

Hybrid environments are common when organisations:

- Have existing data-centre investments.
- Must keep some data on-premises.
- Are migrating gradually.
- Need temporary cloud capacity.

---

### 8.4 Multi-Cloud

A multi-cloud strategy uses services from more than one cloud provider.

An organisation might use:

- AWS for application hosting.
- Microsoft Azure for identity or business systems.
- Google Cloud for analytics.

Multi-cloud can reduce dependence on one provider, but it also increases operational complexity.

---

## 9. Regions and Availability Zones

Cloud providers divide their infrastructure into geographic locations.

### Region

A region is a geographic area containing cloud infrastructure.

Examples might include:

- London
- Ireland
- Frankfurt
- Northern Virginia

Customers choose regions based on factors such as:

- User location
- Latency
- Cost
- Service availability
- Legal requirements
- Data residency

---

### Availability Zone

An Availability Zone is an isolated location within a region.

A region normally contains multiple Availability Zones.

Availability Zones have independent infrastructure, such as:

- Power
- Cooling
- Physical security
- Networking

They are connected using high-speed links.

Deploying across multiple Availability Zones helps protect applications from the failure of one location.

```text
AWS Region
    │
    ├── Availability Zone A
    │       └── Application instance
    │
    ├── Availability Zone B
    │       └── Application instance
    │
    └── Availability Zone C
            └── Database replica
```

---

## 10. High Availability

High availability means designing a service so that it remains accessible despite certain failures.

Imagine an online payment application.

If the application runs on only one server and that server fails, every customer loses access.

A more available design might include:

- Multiple application instances
- Multiple Availability Zones
- A load balancer
- Health checks
- Automated replacement
- Replicated databases

```text
Users
   │
   ▼
Load Balancer
   │
   ├── Healthy instance in Zone A
   │
   └── Healthy instance in Zone B
```

If one instance fails, the load balancer stops sending traffic to it.

High availability does not mean that failure is impossible. It means that the system is designed to reduce downtime and continue operating when expected failures occur.

---

## 11. Scalability

Scalability is the ability of a system to handle increased workload by adding resources.

There are two common forms.

---

### 11.1 Vertical Scaling

Vertical scaling increases the capacity of one machine.

For example:

```text
Before:
2 CPU and 4 GB RAM

After:
8 CPU and 32 GB RAM
```

#### Advantages

- Often simple to implement.
- May require few application changes.

#### Limitations

- Every machine has a maximum size.
- Upgrades may require downtime.
- A single large machine can remain a single point of failure.
- Larger systems may become expensive.

---

### 11.2 Horizontal Scaling

Horizontal scaling adds more machines or application instances.

```text
Before:
One application server

After:
Four application servers behind a load balancer
```

#### Advantages

- Supports large distributed workloads.
- Improves availability when designed correctly.
- Works well with stateless cloud-native applications.
- Capacity can be added gradually.

#### Challenges

- Requires traffic distribution.
- Applications may need shared state or external storage.
- Distributed systems introduce additional complexity.

Horizontal scaling is commonly preferred for cloud-native systems.

---

## 12. Elasticity

Scalability and elasticity are related, but they are not identical.

- **Scalability** describes whether a system can handle growth.
- **Elasticity** describes whether resources can adjust dynamically as demand changes.

Example:

```text
Morning traffic:       2 instances
Lunch traffic:         5 instances
Evening peak:         12 instances
Night-time traffic:    2 instances
```

An elastic system can add and remove resources automatically.

This improves cost efficiency because the system does not need to run at peak capacity all the time.

---

## 13. Fault Tolerance

Fault tolerance is the ability of a system to continue operating when one or more components fail.

It is achieved through techniques such as:

- Redundancy
- Replication
- Automatic failover
- Health checks
- Multiple Availability Zones
- Queue-based communication
- Stateless application design

For example, if one database server fails, a standby database may become active.

Fault-tolerant systems are usually more complex and expensive because they require duplicate or alternative components.

---

## 14. Resilience

Resilience is the ability of a system to withstand failures, recover from them, and continue delivering an acceptable service.

A resilient application may not prevent every failure, but it can:

- Detect the problem.
- Limit the impact.
- Recover automatically.
- Preserve important data.
- Inform operators.
- Return to a healthy state.

Resilience is broader than fault tolerance because it also includes recovery and adaptation.

---

## 15. Disaster Recovery

Disaster recovery focuses on restoring applications and data following a serious disruption.

Examples of disasters include:

- Regional cloud outages
- Cyberattacks
- Accidental deletion
- Database corruption
- Natural disasters
- Major configuration failures

A disaster recovery plan should identify:

- Which systems are most important.
- How data is backed up.
- Where recovery resources are stored.
- Who is responsible for recovery.
- How recovery will be tested.
- How quickly systems must return.

---

### Recovery Time Objective — RTO

RTO describes the maximum acceptable time required to restore a service.

Example:

> The payment system must be restored within one hour.

The RTO is one hour.

---

### Recovery Point Objective — RPO

RPO describes the maximum acceptable amount of data loss measured in time.

Example:

> The organisation can accept losing no more than five minutes of transaction data.

The RPO is five minutes.

---

### Disaster Recovery Strategies

Common strategies include:

#### Backup and Restore

Data is backed up and restored after a disaster.

This is usually the least expensive option but may have a longer recovery time.

#### Pilot Light

A minimal version of the environment remains active, and additional resources are created during recovery.

#### Warm Standby

A smaller but functional copy of the environment runs continuously and is scaled up during a disaster.

#### Multi-Site Active/Active

Multiple environments serve traffic at the same time.

This can provide very fast recovery, but it is expensive and complex.

---

## 16. Security and the Shared Responsibility Model

Moving to the cloud does not remove the customer’s security responsibilities.

Security is shared between the provider and the customer.

### Provider Responsibility: Security of the Cloud

The provider generally protects:

- Data-centre facilities
- Physical servers
- Storage hardware
- Networking infrastructure
- Virtualisation platforms
- Core managed-service infrastructure

---

### Customer Responsibility: Security in the Cloud

The customer may be responsible for:

- User accounts
- IAM permissions
- Application security
- Data classification
- Encryption configuration
- Network rules
- Operating-system patching
- Secrets
- Backups
- Logging and monitoring

The exact responsibility depends on the service model.

For example:

- With EC2, the customer manages the guest operating system.
- With a managed database, the provider manages more of the operating system and database platform.
- With SaaS, the provider manages most of the stack, while the customer still manages users, data access, and configuration.

---

### Example

Suppose an Amazon S3 bucket is accidentally configured for public access.

AWS is responsible for operating and securing the S3 service itself.

The customer is responsible for configuring the bucket and its permissions correctly.

Cloud security failures often happen because customers misunderstand this division of responsibility.

---

## 17. Cloud Pricing Concepts

Cloud computing is often described as pay-as-you-go, but pricing can take several forms.

### On-Demand Pricing

Customers pay for resources without making a long-term commitment.

This provides flexibility but may cost more than discounted options.

---

### Reserved or Committed Usage

Customers commit to a certain level of usage for a longer period in exchange for a lower price.

This is useful for predictable workloads.

---

### Spot or Spare Capacity

Customers use spare provider capacity at a reduced cost.

The provider may reclaim the capacity with limited notice, so it is more suitable for fault-tolerant workloads.

---

### Serverless Consumption Pricing

Customers may pay according to:

- Number of requests
- Execution time
- Memory allocated
- Data processed

---

### Hidden or Easily Missed Costs

Cloud bills may also include:

- Data transfer
- Unused storage
- Public IP addresses
- Logs
- Backups
- Load balancers
- NAT gateways
- Idle development environments

Cost monitoring is an important engineering responsibility.

---

## 18. Cloud-Native Applications

A cloud-hosted application is not automatically cloud-native.

A cloud-native application is designed to use cloud capabilities effectively.

Common cloud-native characteristics include:

- Automated deployment
- Horizontal scaling
- Stateless services
- Containers
- Managed services
- Infrastructure as Code
- Observability
- Resilience
- Continuous delivery
- API-driven architecture

Cloud-native systems are designed with change and failure in mind.

---

## 19. Real-World Example

Consider an online retail application preparing for a major sales event.

Under normal conditions, it may serve a few thousand users.

During the event, traffic may increase dramatically.

A cloud architecture might use:

```text
Customers
    │
    ▼
Content Delivery Network
    │
    ▼
Load Balancer
    │
    ▼
Auto-Scaling Application Instances
    │
    ├── Managed Database
    ├── Object Storage
    ├── Message Queue
    └── Monitoring and Alerts
```

The application can:

- Add instances as traffic increases.
- Remove instances when traffic falls.
- Store static files in object storage.
- Queue background tasks.
- Monitor failures.
- Recover unhealthy instances.
- Run across multiple Availability Zones.

This demonstrates scalability, elasticity, availability, managed services, and measured usage.

---

## 20. How I Have Applied Cloud Computing

### PlatformPilot

PlatformPilot is an AI-assisted Kubernetes Operations Dashboard built using React, FastAPI, and the Kubernetes Python Client.

It currently communicates with a local Kubernetes cluster, but its architecture can be adapted for a managed platform such as Amazon EKS.

Cloud concepts demonstrated by PlatformPilot include:

- API-driven infrastructure access
- Containerised applications
- Kubernetes orchestration
- Monitoring
- Health checks
- Operational automation
- Separation between frontend and backend services

A future cloud deployment could include:

```text
React Frontend
      │
      ▼
Cloud-hosted Web Application
      │
      ▼
FastAPI Backend
      │
      ▼
Amazon EKS
      │
      ▼
Kubernetes Cluster Resources
```

---

### Terraform AWS EKS Platform

In this project, Infrastructure as Code was used to provision cloud resources.

The architecture included concepts such as:

- Amazon EKS
- Virtual Private Cloud networking
- IAM
- Managed node groups
- Security boundaries
- Repeatable deployment
- Automated validation

This project demonstrates how cloud infrastructure can be defined in code instead of being configured manually.

---

### CloudOps Command Center

CloudOps Command Center combines infrastructure, CI/CD, monitoring signals, risk analysis, and operational workflows.

It demonstrates:

- Cloud operations
- Platform Engineering
- API integration
- Infrastructure risk detection
- Audit trails
- Owner routing
- Operational recommendations

---

### Serverless Projects

My Cloud-Native Pharmacy Platform uses Lambda, API Gateway, DynamoDB, Cognito, SQS, EventBridge, CloudWatch, IAM, and AWS SAM. My AI-Powered Content Automation Platform uses Lambda, API Gateway, DynamoDB, EventBridge, Secrets Manager, AWS SAM, and the X API.

In these systems, AWS manages the physical servers, operating-system patching, and much of the runtime scaling. I still own the application code, IAM permissions, data model, authentication, retries, observability, cost controls, and safe handling of failures.

#### How I used serverless architecture in the pharmacy platform

```text
Authenticated client
    -> API Gateway
    -> Lambda application logic
    -> DynamoDB tenant inventory
    -> low-stock event
       |-> SQS -> asynchronous consumer
       `-> EventBridge -> routed consumer
```

- **Problem solved:** process inventory requests and low-stock work without managing permanent application servers.
- **Why Lambda:** event-driven compute matches short API and background-processing tasks.
- **Why DynamoDB:** the project uses tenant-based access patterns suitable for partition-key design.
- **Why SQS:** it buffers asynchronous work and allows retry without keeping the API request open.
- **Why EventBridge:** it routes events to interested targets without tightly coupling producers and consumers.
- **Security responsibility:** Cognito authenticates users, but application code and IAM must still enforce tenant isolation and least privilege.
- **Failure responsibility:** consumers must tolerate duplicate messages, retries, poison messages, and partial failure.
- **Evidence level:** repository documented; infrastructure and application files require full code-level review.

#### How I used serverless architecture in content automation

```text
Browser dashboard
    -> API Gateway
    -> Lambda functions
       |-> DynamoDB plans, queue and activity
       |-> Secrets Manager OAuth tokens
       `-> EventBridge schedule -> publishing Lambda -> X API
```

- **Problem solved:** coordinate planned, queued, manual, and scheduled publishing across multiple accounts.
- **Why EventBridge:** scheduled rules can trigger publishing without a continuously running scheduler server.
- **Why Secrets Manager:** OAuth tokens should not be stored in source code or ordinary configuration files.
- **Why DynamoDB:** publishing state and queue records can be accessed through defined key-based patterns.
- **Operational responsibility:** retries must not create duplicate posts; rate limits and expired tokens must be handled explicitly.
- **Evidence level:** repository documented with deployment screenshots; code-level review remains required.

### Cloud Service Models Across My Projects

My projects combine service models rather than fitting into only one category:

| Project | Cloud model demonstrated | My responsibility |
|---|---|---|
| Pharmacy API on EKS | Managed Kubernetes with container workloads | Application, images, Kubernetes resources, IAM, networking decisions and workload operations |
| Terraform EKS | Infrastructure as Code for managed cloud infrastructure | Terraform definitions, state, access, configuration, validation and lifecycle |
| Cloud-Native Pharmacy | Serverless managed services | Functions, data model, authentication, permissions, events, retries and observability |
| OpsPilot | SaaS-style application using managed identity, database and hosting services | Product code, tenant isolation, roles, data, billing workflow and application reliability |
| AI Content Automation | Serverless event-driven platform | OAuth, Lambda logic, schedules, queue state, permissions and operational safeguards |

### What I Must Be Able to Explain

Before claiming cloud experience from these projects, I should be able to:

- draw the architecture without reading the README;
- identify which components are managed by AWS and which remain my responsibility;
- trace one request or event from beginning to end;
- explain the IAM identity used at every AWS boundary;
- describe what happens when a dependency fails;
- explain how the system is deployed and updated;
- identify its main cost drivers;
- distinguish evidence in the repository from planned improvements;
- compare the EKS and serverless approaches used by the two pharmacy projects.

For the complete cross-project mapping, see the [Technology-to-Project Evidence Map](../TECHNOLOGY-PROJECT-MAP.md).

---

## 21. Best Practices

### Design for Failure

Assume that individual resources can fail.

Use:

- Health checks
- Redundancy
- Automated recovery
- Backups
- Multiple Availability Zones

---

### Automate Infrastructure

Use Infrastructure as Code instead of relying only on manual console changes.

Benefits include:

- Repeatability
- Version control
- Reviewability
- Faster recovery
- Reduced configuration drift

---

### Apply Least Privilege

Users, applications, and services should receive only the permissions they require.

Avoid broad administrative access where possible.

---

### Monitor Continuously

Collect:

- Metrics
- Logs
- Traces
- Audit events
- Cost data
- Security findings

Monitoring should help detect failures before users report them.

---

### Tag Resources

Apply consistent tags such as:

- Environment
- Owner
- Application
- Cost centre
- Managed-by
- Project

Tags improve ownership, governance, automation, and cost reporting.

---

### Control Costs

Regularly review:

- Idle resources
- Oversized instances
- Storage growth
- Data-transfer charges
- Unused load balancers
- Old snapshots
- Logging retention

---

### Protect Data

Use:

- Encryption
- Backups
- Access controls
- Retention policies
- Replication where required
- Tested recovery procedures

---

### Prefer Managed Services When Appropriate

Managed services can reduce operational overhead, but they may introduce:

- Additional cost
- Service limitations
- Vendor dependence
- Migration complexity

Choose services based on requirements rather than popularity.

---

## 22. Common Mistakes

### Assuming the Cloud Is Automatically Secure

The provider secures the underlying platform, but customers must configure identities, networks, applications, and data correctly.

---

### Overprovisioning

Creating resources larger than necessary increases cost without always improving performance.

---

### Ignoring Cost Until the End

Cost should be considered during architecture and development, not only after deployment.

---

### Using One Availability Zone

A single-zone architecture may fail completely if that zone becomes unavailable.

---

### Relying on Manual Changes

Manual configuration can create inconsistency and make recovery more difficult.

---

### Failing to Test Backups

A backup is useful only if it can be restored successfully.

---

### Confusing Scalability with Elasticity

A scalable system can grow.

An elastic system adjusts capacity dynamically as demand changes.

---

### Moving an Application Without Redesigning It

Simply copying a traditional application to a cloud virtual machine may not provide the full benefits of cloud computing.

---

## 23. Interview Questions and Answers

### What is cloud computing?

Cloud computing is the on-demand delivery of computing resources such as servers, storage, databases, networking, and software over a network. It allows customers to provision resources quickly, adjust capacity when needed, and avoid owning all the underlying physical infrastructure.

---

### Why do organisations use cloud computing?

Organisations use cloud computing to reduce upfront infrastructure costs, provision resources faster, scale applications, deploy globally, improve availability, automate infrastructure, and use managed services.

---

### What is the difference between IaaS, PaaS, and SaaS?

- **IaaS** provides infrastructure such as virtual machines, storage, and networking. The customer manages the operating system and application.
- **PaaS** provides a managed application platform. The customer focuses mainly on code and data.
- **SaaS** provides a complete application managed by the provider.

---

### What is the difference between scalability and elasticity?

Scalability is the ability of a system to handle increasing workload by adding resources.

Elasticity is the ability to add and remove resources dynamically as demand changes.

---

### What is high availability?

High availability is the practice of designing systems so they remain accessible despite certain component failures. It often involves multiple instances, health checks, load balancing, and deployment across independent locations.

---

### What is fault tolerance?

Fault tolerance is the ability of a system to continue operating when one or more components fail. It generally requires redundancy, replication, and automatic failover.

---

### What is the shared responsibility model?

The shared responsibility model divides security duties between the cloud provider and the customer. The provider secures the underlying cloud infrastructure, while the customer secures their data, identities, applications, permissions, and configurations according to the service being used.

---

### What is horizontal scaling?

Horizontal scaling adds more machines or application instances to handle increased workload.

---

### What is vertical scaling?

Vertical scaling increases the CPU, memory, or another resource of an existing machine.

---

### What is a cloud region?

A cloud region is a geographic area where a provider operates infrastructure. It normally contains multiple isolated Availability Zones.

---

### What are RTO and RPO?

- **RTO** is the maximum acceptable time required to restore a service.
- **RPO** is the maximum acceptable amount of data loss measured in time.

---

### What is Infrastructure as Code?

Infrastructure as Code is the practice of defining and managing infrastructure using machine-readable configuration files. Tools such as Terraform and CloudFormation make infrastructure repeatable, version-controlled, and automatable.

---

### Is cloud computing always cheaper than on-premises infrastructure?

No. Cloud computing provides flexibility and can reduce upfront costs, but poor architecture, idle resources, unnecessary data transfer, and weak cost controls can make it expensive.

---

### What is a cloud-native application?

A cloud-native application is designed to take advantage of cloud capabilities such as automated deployment, elasticity, managed services, observability, resilience, containers, and distributed architecture.

---

## 24. Review Questions

Try to answer these without looking back at the chapter:

1. What problem did cloud computing solve?
2. What are the five main characteristics of cloud computing?
3. How does IaaS differ from PaaS?
4. What is the difference between public and private cloud?
5. Why are Availability Zones important?
6. What is the difference between horizontal and vertical scaling?
7. How is elasticity different from scalability?
8. What is the purpose of disaster recovery?
9. What do RTO and RPO measure?
10. Which security responsibilities normally remain with the customer?
11. Why is Infrastructure as Code useful?
12. What makes an application cloud-native?
13. Where have you applied cloud concepts in your own projects?

---

## 25. Practical Exercises

### Exercise 1 — Classify Services

Decide whether each example is mainly IaaS, PaaS, or SaaS:

- Amazon EC2
- Microsoft 365
- Azure App Service
- Gmail
- Google Compute Engine
- AWS Elastic Beanstalk

---

### Exercise 2 — Design for Availability

Draw a simple application architecture containing:

- Two Availability Zones
- Two application instances
- One load balancer
- A replicated database
- Monitoring

Explain what happens if one application instance fails.

---

### Exercise 3 — Scaling Decision

An application is running slowly because it receives ten times more traffic during weekends.

Explain:

- How vertical scaling might help.
- How horizontal scaling might help.
- How elasticity could reduce cost during quieter periods.

---

### Exercise 4 — Shared Responsibility

For an EC2-hosted web application, identify whether the provider or customer is mainly responsible for:

- Physical data-centre security
- Guest operating-system patching
- IAM permissions
- Application vulnerabilities
- Physical server replacement
- Data encryption configuration
- Security-group rules

---

### Exercise 5 — Project Reflection

Write a short explanation of how one of your projects uses cloud principles.

Suggested projects:

- PlatformPilot
- Terraform AWS EKS Platform
- CloudOps Command Center
- AI-Powered Content Automation Platform
- Cloud-Native Pharmacy Platform

---

## 26. Key Takeaways

After completing this chapter, you should understand that:

- Cloud computing provides computing resources on demand.
- Customers can provision infrastructure without buying all the underlying hardware.
- Cloud platforms support faster delivery, global reach, automation, and managed services.
- IaaS, PaaS, and SaaS provide different levels of customer control and responsibility.
- Public, private, hybrid, and multi-cloud models support different organisational needs.
- Scalability allows a system to grow.
- Elasticity allows capacity to adjust dynamically.
- High availability reduces downtime.
- Fault tolerance helps systems continue operating during failures.
- Disaster recovery prepares organisations for serious disruptions.
- Cloud security remains a shared responsibility.
- Cloud costs must be monitored and actively managed.
- Cloud-native systems are designed for automation, resilience, observability, and change.

---

## 27. Chapter Summary

Cloud computing changed technology by making infrastructure and managed services available on demand.

Instead of purchasing and maintaining every physical component, organisations can provision compute, storage, databases, networking, and many other services through consoles, APIs, command-line tools, and Infrastructure as Code.

However, cloud computing is not simply a different place to run servers.

Using the cloud effectively requires engineers to understand:

- Responsibility
- Security
- Availability
- Scaling
- Automation
- Cost
- Recovery
- Observability
- Architecture

The cloud provider supplies powerful capabilities, but good outcomes still depend on good engineering decisions.

Cloud computing forms the foundation for many of the technologies covered later in this handbook, including Docker, Kubernetes, AWS, Terraform, CI/CD, observability, and Platform Engineering.

---

## Next Chapter

In **Chapter 2 — Linux Fundamentals**, we move from cloud infrastructure to the operating system that powers much of it.

You will learn about:

- The Linux architecture
- The filesystem
- Files and directories
- Users and groups
- Permissions
- Processes
- Services
- Networking
- Logs
- SSH
- Bash
- Troubleshooting
- Essential commands for Cloud and Platform Engineers
