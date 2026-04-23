# Self-Hosted SCM & Artifacts - Devin Docs

Source: https://docs.devin.ai/integrations/self-hosted-scm-artifacts

- Support

- Devin

- Devin

- Introducing Devin

- Your First Session

- Tutorial Library

- When to Use Devin

- Instructing Devin Effectively

- Good vs. Bad Instructions

- Prompt Templates Cheat Sheet

- How does Devin fit into my existing SDLC?

- Environment configuration

- Index a Repository

- VPN Configuration

- Knowledge Onboarding

- AGENTS.md

- Devin Review

- Devin Session Tools

- Computer Use

- Testing & Video Recordings

- Slash Commands

- Ask Devin

- Data Analyst Agent

- DeepWiki

- MCP (Model Context Protocol) Marketplace

- DeepWiki MCP

- Devin MCP

- Advanced Capabilities

- Knowledge

- Skills

- Session Insights

- Secrets & Site Cookies

- Creating Playbooks

- Using Playbooks

- Scheduled Sessions

- Deployments

- Autofix Settings - Bot Comments

- Invite your Team

- Importing Code Settings

- Integrations Overview

- Slack

- Microsoft Teams

- GitHub

- GitLab

- Bitbucket

- Linear

- Jira

- GitHub Pull Request Templates

- Self-Hosted SCM & Artifacts

- Security at Cognition

- Billing

- Common Issues

- Why connect Devin to self-hosted systems?

- Overview

- Prerequisites

- Setup Options

- Option 1: Direct IP Whitelisting (Recommended)

- Option 2: Centralized Load Balancer

- Load Balancer Considerations

- AWS Implementation Example

- Application Load Balancer with WAF (Easier)

- Network Load Balancer (Manual Security Groups)

- DNS Configuration

- Integration Steps

- Best Practices

- Troubleshooting

- Support

# Self-Hosted SCM & Artifacts

Connect Devin SaaS to your self-hosted source code management and artifact repositories

## ​ Why connect Devin to self-hosted systems?

## ​ Overview

- Limits access to a small, controlled surface area - Only Devin’s known IPs can connect

- Takes less than a few hours of engineering effort to set up

- Maintains your existing infrastructure - No need to migrate to cloud-hosted solutions

- Provides centralized management - Optional single load balancer for multiple services

## ​ Prerequisites

- Self-hosted GitLab (or other SCM system) accessible within your network

- Self-hosted artifact repository (optional) such as Artifactory or Nexus

- Network administration access to configure firewalls, load balancers, and DNS

- Devin’s static IP addresses - Found here

## ​ Setup Options

### ​ Option 1: Direct IP Whitelisting (Recommended)

- Configure your firewall to allow inbound connections from Devin’s IPs (listed here )

- Ensure your GitLab (or other SCM) instance is accessible via HTTPS

- Provide the URL to Devin during integration setup

- Add Devin’s IPs to your Artifactory/Nexus allowlist

- Ensure the artifact repository is accessible via HTTPS

- Configure appropriate credentials for Devin to access artifacts

### ​ Option 2: Centralized Load Balancer

- Single point of management for all network filtering

- Support multiple internal services with different domains

- Simplified security auditing and compliance

## ​ Load Balancer Considerations

- ALB operates at Layer 7 (HTTP/HTTPS) and provides advanced routing capabilities

- Traffic goes through NAT, so your backend services see the ALB’s internal IP addresses, not Devin’s source IPs

- For artifact repositories behind ALB: You must configure IP allowlisting directly on Artifactory/Nexus since the load balancer’s internal IP will be seen by the repository

- Use AWS WAF for IP filtering at the ALB level (see example below)

- NLB operates at Layer 4 (TCP) and preserves the original source IP addresses

- Your backend services see Devin’s actual source IPs

- For artifact repositories behind NLB: IP allowlisting at the load balancer level is sufficient since source IPs are maintained

- Requires manual security group configuration for each IP address

## ​ AWS Implementation Example

### ​ Application Load Balancer with WAF (Easier)

```
# Create an IP set with Devin's static IPs aws wafv2 create-ip-set \ --name devin-allowed-ips \ --scope REGIONAL \ --ip-address-version IPV4 \ --addresses 1.2.3.4/32 5.6.7.8/32 9.10.11.12/32 13.14.15.16/32 # Create a WAF web ACL aws wafv2 create-web-acl \ --name devin-access-control \ --scope REGIONAL \ --default-action Block={} \ --rules file://waf-rules.json # Associate the WAF with your ALB aws wafv2 associate-web-acl \ --web-acl-arn arn:aws:wafv2:region:account:regional/webacl/... \ --resource-arn arn:aws:elasticloadbalancing:region:account:loadbalancer/app/...
```

```
# Create an IP set with Devin's static IPs aws wafv2 create-ip-set \ --name devin-allowed-ips \ --scope REGIONAL \ --ip-address-version IPV4 \ --addresses 1.2.3.4/32 5.6.7.8/32 9.10.11.12/32 13.14.15.16/32 # Create a WAF web ACL aws wafv2 create-web-acl \ --name devin-access-control \ --scope REGIONAL \ --default-action Block={} \ --rules file://waf-rules.json # Associate the WAF with your ALB aws wafv2 associate-web-acl \ --web-acl-arn arn:aws:wafv2:region:account:regional/webacl/... \ --resource-arn arn:aws:elasticloadbalancing:region:account:loadbalancer/app/...
```

### ​ Network Load Balancer (Manual Security Groups)

```
# Add ingress rules for each Devin IP to your security group aws ec2 authorize-security-group-ingress \ --group-id sg-xxxxxxxxx \ --protocol tcp \ --port 443 \ --cidr 1.2.3.4/32 # Repeat for each IP address aws ec2 authorize-security-group-ingress \ --group-id sg-xxxxxxxxx \ --protocol tcp \ --port 443 \ --cidr 5.6.7.8/32 # Continue for all Devin IPs...
```

```
# Add ingress rules for each Devin IP to your security group aws ec2 authorize-security-group-ingress \ --group-id sg-xxxxxxxxx \ --protocol tcp \ --port 443 \ --cidr 1.2.3.4/32 # Repeat for each IP address aws ec2 authorize-security-group-ingress \ --group-id sg-xxxxxxxxx \ --protocol tcp \ --port 443 \ --cidr 5.6.7.8/32 # Continue for all Devin IPs...
```

### ​ DNS Configuration

```
# Example: Point gitlab.yourcompany.com to your load balancer # The domain will resolve to the load balancer IP, which filters traffic # to only allow connections from Devin's whitelisted IPs # Using AWS Route 53: aws route53 change-resource-record-sets \ --hosted-zone-id Z1234567890ABC \ --change-batch file://dns-change.json
```

```
# Example: Point gitlab.yourcompany.com to your load balancer # The domain will resolve to the load balancer IP, which filters traffic # to only allow connections from Devin's whitelisted IPs # Using AWS Route 53: aws route53 change-resource-record-sets \ --hosted-zone-id Z1234567890ABC \ --change-batch file://dns-change.json
```

```
dns-change.json
```

```
{ "Changes" : [{ "Action" : "CREATE" , "ResourceRecordSet" : { "Name" : "gitlab.yourcompany.com" , "Type" : "A" , "AliasTarget" : { "HostedZoneId" : "Z215JYRZR1TBD5" , "DNSName" : "your-alb-name-123456.us-west-2.elb.amazonaws.com" , "EvaluateTargetHealth" : false } } }] }
```

```
{ "Changes" : [{ "Action" : "CREATE" , "ResourceRecordSet" : { "Name" : "gitlab.yourcompany.com" , "Type" : "A" , "AliasTarget" : { "HostedZoneId" : "Z215JYRZR1TBD5" , "DNSName" : "your-alb-name-123456.us-west-2.elb.amazonaws.com" , "EvaluateTargetHealth" : false } } }] }
```

## ​ Integration Steps

- Test connectivity - Verify that your services are accessible from outside your network using the configured domain

- Contact Devin support - Reach out to Cognition with: Your self-hosted GitLab URL (e.g., https://gitlab.yourcompany.com ) Your artifact repository URL (if applicable) Any specific authentication requirements

- Your self-hosted GitLab URL (e.g., https://gitlab.yourcompany.com )

```
https://gitlab.yourcompany.com
```

- Your artifact repository URL (if applicable)

- Any specific authentication requirements

- Complete integration setup - Work with the Devin team to finalize the connection

- Configure repositories - Add your repositories to Devin’s Machine

## ​ Best Practices

- Use HTTPS - Always expose services over HTTPS with valid SSL certificates

- Create a dedicated service account - Set up a specific account for Devin in your GitLab/SCM system

- Monitor access logs - Regularly review connection logs from Devin’s IPs

- Document your setup - Keep internal documentation of your load balancer and DNS configuration

- Test failover - Ensure your setup can handle load balancer or service failures gracefully

- Regular security audits - Periodically review which services are exposed and verify IP allowlists

## ​ Troubleshooting

- Verify that all Devin IP addresses are whitelisted

- Check that your SSL certificate is valid and trusted

- Ensure DNS records are properly configured and propagated

- Verify your firewall rules allow HTTPS (port 443) traffic

- Confirm the service account credentials are correct

- Verify the service account has appropriate permissions in your SCM/artifact system

- Check for any IP-based authentication restrictions beyond the allowlist

- Monitor your load balancer metrics for bottlenecks

- Ensure your self-hosted services have adequate resources

- Consider geographic proximity between your infrastructure and Devin’s systems

## ​ Support

- Create a Slack Connect channel with our team at app.devin.ai/settings/support

- Email enterprise@cognition.ai with your specific setup details

- Share relevant configuration files (with sensitive data redacted) when reporting issues
