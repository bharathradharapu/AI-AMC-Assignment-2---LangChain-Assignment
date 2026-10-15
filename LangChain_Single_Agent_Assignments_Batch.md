# LangChain Single-Agent Assignments

## Overview

You have been given a working LangChain agent project — **Email Humanizer** — as your reference implementation. Your task is to **build your own unique use case** using the exact same framework and patterns.

Study the `email_humanizer_agent.py` file carefully. Your agent must follow this structure:

```text
[User Input] --> [Tool 1] --> [Tool 2] --> [Final Output]
```

Each student below has been assigned a unique agent. Build the agent assigned to your name. Do not swap assignments or copy another student's use case.

---

## What You Must Build

Use the same LangChain patterns as the reference code:

- `ChatOpenAI` — the LLM
- `PromptTemplate` — to shape LLM responses
- `@tool` decorator — to define at least two tools
- `create_agent` — to wire everything together
- A `SYSTEM_PROMPT` — to define agent behaviour
- A `run_<your_agent>()` function — as the main entry point
- A simple CLI loop in `main()` — so anyone can run and test your agent

---

## Submission Steps

1. Fork or clone the reference repository.
2. Create your own Python file. Do not modify `email_humanizer_agent.py`.
3. Build your assigned use case using the required structure.
4. Test it end-to-end with your OpenAI API key.
5. Push your code to a new public GitHub repository under your own account.
6. Share the GitHub repository link in the Excel sheet shared on WhatsApp.

Your repository must contain your agent `.py` file, `requirements.txt`, `.env.example`, `.gitignore`, and a clear `README.md`. Never commit your real `.env` file or API key.

---

## Student List

| No. | Name | Email |
|---:|---|---|
| 1 | Nidhi Mittal | Nidhi.goyal78@gmail.com |
| 2 | Jitendra Kumar Saroj | jitendra.saroj007@gmail.com |
| 3 | Vivek Harle | Vivek.harle1@gmail.com |
| 4 | Aditya Venkata Satyanarayana Mokkapati | adityamokkapati@gmail.com |
| 5 | Radharapu Bharath Kumar | bharathradharapu.1989@gmail.com |
| 6 | Avinash Dupaguntla | avinashd1276@gmail.com |
| 7 | Kailas Kanade | kailasukanade@gmail.com |
| 8 | Raviraj Deshpande | deshpande.raviraj@gmail.com |
| 9 | Sheetal Deshpande | rdeshpande.sheetal@gmail.com |
| 10 | Vishal Kailas Kharade | vishalkharade02@gmail.com |
| 11 | Usama Mirkar | mirkarusamaa@gmail.com |
| 12 | Hariharan | hareharankrish@gmail.com |
| 13 | Harmeet Bedi | hsbedi06@gmail.com |
| 14 | Valathappan Sivaraman | Valathappan@gmail.com |
| 15 | Balaji Kumar | Balajitkumar2@gmail.com |
| 16 | Surendran Sundarababu | ganeshh.suren@gmail.com |
| 17 | Mohit Luthra | manmohitluthra@gmail.com |
| 18 | Shirish Suryakant Pathak | shirishpathak86@gmail.com |
| 19 | Bhanupriya | Banupriya.uipath@gmail.com |
| 20 | Jolly Shringi | jollyshringi.888@gmaill.com |

> **Check required:** Jolly Shringi's email is reproduced exactly as provided. Confirm whether `gmaill.com` should be `gmail.com` before using it.

---

## Individual Assignments

### 1. Nidhi Mittal — Meeting Notes Action Agent

**Email:** Nidhi.goyal78@gmail.com  
**Python file:** `meeting_notes_agent.py`

**Use Case:** Convert raw meeting notes into a structured summary and an actionable follow-up plan.

**Tool 1 — `extract_meeting_insights`**
- Input: Raw meeting notes or transcript
- Task: Identify decisions, key discussion points, risks, open questions, owners, and deadlines
- Output: A structured meeting summary

**Tool 2 — `create_action_plan`**
- Input: Structured summary from Tool 1
- Task: Turn commitments into action items with owner, priority, deadline, and status
- Output: A Markdown action tracker and follow-up summary

**System Prompt:** Act as a precise meeting facilitator. Always use Tool 1 before Tool 2, preserve facts, and never invent owners or deadlines.

---

### 2. Jitendra Kumar Saroj — Resume Improvement Agent

**Email:** jitendra.saroj007@gmail.com  
**Python file:** `resume_improvement_agent.py`

**Use Case:** Review resume content against a target role and rewrite weak sections for relevance and impact.

**Tool 1 — `analyze_resume_gaps`**
- Input: Resume text and target job description
- Task: Find missing keywords, vague statements, repetition, weak evidence, and relevant skill gaps
- Output: A prioritized gap analysis

**Tool 2 — `rewrite_resume_sections`**
- Input: Gap analysis and original resume
- Task: Rewrite the summary, skills, and experience bullets using concise, truthful, impact-first language
- Output: Improved resume sections in Markdown

**System Prompt:** Act as an ethical technical recruiter. Always use Tool 1 before Tool 2 and never fabricate skills, experience, or metrics.

---

### 3. Vivek Harle — Code Review Assistant Agent

**Email:** Vivek.harle1@gmail.com  
**Python file:** `code_review_agent.py`

**Use Case:** Analyze pasted code for quality and risks, then produce a prioritized review with fixes.

**Tool 1 — `inspect_code_quality`**
- Input: Source code and optional language/framework details
- Task: Identify correctness, readability, security, maintainability, and performance concerns
- Output: Findings grouped by severity with evidence

**Tool 2 — `write_review_recommendations`**
- Input: Findings from Tool 1
- Task: Propose practical fixes and improved snippets for the most important issues
- Output: A concise code-review report

**System Prompt:** Act as a constructive senior engineer. Always use Tool 1 before Tool 2 and avoid presenting unverified concerns as confirmed bugs.

---

### 4. Aditya Venkata Satyanarayana Mokkapati — API Test Case Generator Agent

**Email:** adityamokkapati@gmail.com  
**Python file:** `api_test_case_agent.py`

**Use Case:** Convert an API specification or endpoint description into comprehensive test scenarios.

**Tool 1 — `analyze_api_contract`**
- Input: Endpoint, method, parameters, headers, body, and expected responses
- Task: Extract validation rules, dependencies, success paths, and possible failure conditions
- Output: A structured API contract analysis

**Tool 2 — `generate_api_test_cases`**
- Input: Contract analysis from Tool 1
- Task: Create positive, negative, boundary, authorization, and error-handling cases
- Output: A Markdown table with case ID, input, steps, expected status, and result

**System Prompt:** Act as a senior API QA engineer. Always use Tool 1 before Tool 2 and make every test case independently executable.

---

### 5. Radharapu Bharath Kumar — Incident Triage Agent

**Email:** bharathradharapu.1989@gmail.com  
**Python file:** `incident_triage_agent.py`

**Use Case:** Analyze an incident description and logs, then create a practical investigation and response plan.

**Tool 1 — `classify_incident`**
- Input: Incident description, symptoms, logs, and affected services
- Task: Determine likely category, business impact, urgency, and probable causes
- Output: Severity recommendation and ranked hypotheses

**Tool 2 — `create_incident_response_plan`**
- Input: Classification from Tool 1
- Task: Produce immediate containment, diagnostic, communication, and recovery actions
- Output: A prioritized incident-response checklist

**System Prompt:** Act as a calm production incident commander. Always use Tool 1 before Tool 2 and distinguish confirmed facts from hypotheses.

---

### 6. Avinash Dupaguntla — SQL Query Builder Agent

**Email:** avinashd1276@gmail.com  
**Python file:** `sql_query_builder_agent.py`

**Use Case:** Convert a natural-language reporting request into a validated SQL query and explanation.

**Tool 1 — `plan_sql_query`**
- Input: User request, database dialect, and table schemas
- Task: Identify tables, joins, filters, aggregations, grouping, and edge cases
- Output: A structured query plan

**Tool 2 — `generate_sql_query`**
- Input: Query plan from Tool 1
- Task: Write safe, readable SQL and explain assumptions and result columns
- Output: Executable SQL plus a short explanation

**System Prompt:** Act as a careful analytics engineer. Always use Tool 1 before Tool 2, use only supplied fields, and never generate destructive SQL.

---

### 7. Kailas Kanade — Learning Roadmap Agent

**Email:** kailasukanade@gmail.com  
**Python file:** `learning_roadmap_agent.py`

**Use Case:** Build a personalized learning plan from a learner's goal, current skills, and available time.

**Tool 1 — `assess_learning_gap`**
- Input: Target skill, current level, deadline, and weekly availability
- Task: Identify prerequisites, strengths, gaps, and realistic milestones
- Output: A structured learning-gap assessment

**Tool 2 — `build_learning_roadmap`**
- Input: Assessment from Tool 1
- Task: Create a week-by-week roadmap with topics, practice tasks, mini-projects, and checkpoints
- Output: A personalized learning plan in Markdown

**System Prompt:** Act as a practical technical mentor. Always use Tool 1 before Tool 2 and keep the plan achievable within the stated time.

---

### 8. Raviraj Deshpande — Customer Complaint Response Agent

**Email:** deshpande.raviraj@gmail.com  
**Python file:** `complaint_response_agent.py`

**Use Case:** Analyze a customer complaint and draft a professional, empathetic resolution response.

**Tool 1 — `analyze_customer_complaint`**
- Input: Customer message and service context
- Task: Identify the core issue, sentiment, requested outcome, urgency, and missing information
- Output: A complaint analysis and response strategy

**Tool 2 — `draft_resolution_response`**
- Input: Analysis from Tool 1
- Task: Acknowledge the issue, explain next steps, and avoid unsupported promises
- Output: A ready-to-send customer response

**System Prompt:** Act as an experienced customer-care lead. Always use Tool 1 before Tool 2, sound human, and never blame the customer.

---

### 9. Sheetal Deshpande — Personal Budget Planner Agent

**Email:** rdeshpande.sheetal@gmail.com  
**Python file:** `personal_budget_agent.py`

**Use Case:** Analyze monthly income and expenses, then create a realistic budget and savings plan.

**Tool 1 — `analyze_spending`**
- Input: Income, fixed costs, variable expenses, debts, and savings goals
- Task: Categorize spending, calculate totals, and identify pressure points
- Output: A financial snapshot with percentages and observations

**Tool 2 — `create_monthly_budget`**
- Input: Financial snapshot from Tool 1
- Task: Allocate a sustainable monthly budget and suggest measurable savings actions
- Output: A budget table and monthly action plan

**System Prompt:** Act as a cautious budgeting coach, not a financial adviser. Always use Tool 1 before Tool 2 and label assumptions.

---

### 10. Vishal Kailas Kharade — Job Interview Coach Agent

**Email:** vishalkharade02@gmail.com  
**Python file:** `interview_coach_agent.py`

**Use Case:** Analyze a target job description and prepare tailored interview questions and answer frameworks.

**Tool 1 — `analyze_target_role`**
- Input: Job description and candidate profile
- Task: Identify critical skills, likely interview themes, strengths, and preparation gaps
- Output: A role-readiness assessment

**Tool 2 — `prepare_interview_pack`**
- Input: Assessment from Tool 1
- Task: Generate technical and behavioural questions with STAR-style guidance and follow-up probes
- Output: A personalized interview practice pack

**System Prompt:** Act as a rigorous interview coach. Always use Tool 1 before Tool 2 and use only the candidate experience provided.

---

### 11. Usama Mirkar — Product Description Writer Agent

**Email:** mirkarusamaa@gmail.com  
**Python file:** `product_description_agent.py`

**Use Case:** Turn raw product details into persuasive and accurate e-commerce copy.

**Tool 1 — `extract_product_value`**
- Input: Product specifications, target customer, and brand tone
- Task: Separate features, benefits, differentiators, proof points, and missing information
- Output: A structured product value map

**Tool 2 — `write_product_listing`**
- Input: Value map from Tool 1
- Task: Create a title, summary, benefit bullets, detailed description, and SEO meta description
- Output: A ready-to-publish product listing

**System Prompt:** Act as an honest conversion copywriter. Always use Tool 1 before Tool 2 and never invent product capabilities.

---

### 12. Hariharan — Log Error Explainer Agent

**Email:** hareharankrish@gmail.com  
**Python file:** `log_error_explainer_agent.py`

**Use Case:** Convert confusing application logs into a clear diagnosis and debugging checklist.

**Tool 1 — `analyze_error_logs`**
- Input: Logs, stack trace, runtime context, and recent changes
- Task: Extract the primary error, warnings, affected component, and ranked root-cause hypotheses
- Output: A plain-language diagnostic summary

**Tool 2 — `create_debugging_steps`**
- Input: Diagnostic summary from Tool 1
- Task: Produce safe verification steps and fixes ordered from least to most invasive
- Output: A step-by-step debugging checklist

**System Prompt:** Act as a methodical support engineer. Always use Tool 1 before Tool 2 and never present a hypothesis as a confirmed cause.

---

### 13. Harmeet Bedi — Travel Itinerary Planner Agent

**Email:** hsbedi06@gmail.com  
**Python file:** `travel_itinerary_agent.py`

**Use Case:** Convert trip preferences into a balanced, day-by-day travel itinerary.

**Tool 1 — `analyze_trip_preferences`**
- Input: Destination, dates, budget, interests, pace, group details, and constraints
- Task: Determine priorities, geographic grouping, timing needs, and planning constraints
- Output: A trip-planning profile

**Tool 2 — `build_daily_itinerary`**
- Input: Trip profile from Tool 1
- Task: Create a daily itinerary with morning, afternoon, evening, travel buffers, and estimated costs
- Output: A practical Markdown itinerary

**System Prompt:** Act as a thoughtful travel planner. Always use Tool 1 before Tool 2, avoid claiming live availability, and label estimates.

---

### 14. Valathappan Sivaraman — Fitness Routine Planner Agent

**Email:** Valathappan@gmail.com  
**Python file:** `fitness_routine_agent.py`

**Use Case:** Build a safe beginner exercise plan based on goals, schedule, equipment, and limitations.

**Tool 1 — `assess_fitness_requirements`**
- Input: Goal, experience, available days, equipment, and stated limitations
- Task: Identify suitable training focus, volume, recovery needs, and safety constraints
- Output: A fitness requirements profile

**Tool 2 — `create_workout_schedule`**
- Input: Requirements profile from Tool 1
- Task: Produce a weekly routine with exercises, sets, repetitions, rest, warm-up, and progression
- Output: A structured workout plan

**System Prompt:** Act as a conservative general fitness coach, not a medical professional. Always use Tool 1 before Tool 2 and advise professional guidance for pain or medical concerns.

---

### 15. Balaji Kumar — Email Campaign Planner Agent

**Email:** Balajitkumar2@gmail.com  
**Python file:** `email_campaign_agent.py`

**Use Case:** Turn a campaign goal into an audience strategy and a short email sequence.

**Tool 1 — `design_campaign_strategy`**
- Input: Offer, target audience, campaign goal, brand tone, and desired action
- Task: Define pain points, value proposition, objections, sequence logic, and success metric
- Output: A structured campaign brief

**Tool 2 — `write_email_sequence`**
- Input: Campaign brief from Tool 1
- Task: Write three concise emails with subject lines, preview text, body copy, and calls to action
- Output: A ready-to-use email sequence

**System Prompt:** Act as a permission-based email marketer. Always use Tool 1 before Tool 2 and avoid deceptive or unsupported claims.

---

### 16. Surendran Sundarababu — Requirements Clarifier Agent

**Email:** ganeshh.suren@gmail.com  
**Python file:** `requirements_clarifier_agent.py`

**Use Case:** Transform a vague software request into clear, implementation-ready requirements.

**Tool 1 — `identify_requirement_gaps`**
- Input: Raw stakeholder request
- Task: Extract goals, users, scope, constraints, dependencies, ambiguities, and unanswered questions
- Output: A gap report with prioritized questions

**Tool 2 — `write_structured_requirements`**
- Input: Gap report and available stakeholder details
- Task: Draft functional and non-functional requirements, assumptions, exclusions, and acceptance conditions
- Output: A concise requirements specification

**System Prompt:** Act as a senior business analyst. Always use Tool 1 before Tool 2 and mark unresolved items instead of inventing answers.

---

### 17. Mohit Luthra — Data Cleaning Advisor Agent

**Email:** manmohitluthra@gmail.com  
**Python file:** `data_cleaning_agent.py`

**Use Case:** Analyze a dataset description or sample and produce a safe, reproducible cleaning plan.

**Tool 1 — `profile_data_quality`**
- Input: Dataset sample, column descriptions, and intended use
- Task: Identify missing values, duplicates, invalid types, inconsistent formats, outliers, and risky fields
- Output: A prioritized data-quality report

**Tool 2 — `create_cleaning_recipe`**
- Input: Data-quality report from Tool 1
- Task: Define ordered cleaning operations, validation checks, and optional pandas examples
- Output: A reproducible cleaning recipe

**System Prompt:** Act as a careful data engineer. Always use Tool 1 before Tool 2 and preserve raw data through non-destructive transformations.

---

### 18. Shirish Suryakant Pathak — Risk Register Generator Agent

**Email:** shirishpathak86@gmail.com  
**Python file:** `risk_register_agent.py`

**Use Case:** Analyze a project plan and produce a prioritized risk register with mitigation actions.

**Tool 1 — `identify_project_risks`**
- Input: Project description, timeline, dependencies, team, and constraints
- Task: Identify technical, delivery, operational, security, and stakeholder risks
- Output: Risks with likelihood, impact, evidence, and category

**Tool 2 — `build_risk_register`**
- Input: Risks from Tool 1
- Task: Assign severity, preventive actions, contingency steps, suggested owners, and review triggers
- Output: A Markdown risk-register table

**System Prompt:** Act as a pragmatic project risk manager. Always use Tool 1 before Tool 2 and label suggested owners or assumptions.

---

### 19. Bhanupriya — Study Quiz Generator Agent

**Email:** Banupriya.uipath@gmail.com  
**Python file:** `study_quiz_agent.py`

**Use Case:** Turn study material into a balanced quiz and detailed answer guide.

**Tool 1 — `extract_learning_objectives`**
- Input: Notes, article, or lesson content
- Task: Identify key concepts, facts, relationships, and appropriate difficulty levels
- Output: A structured set of learning objectives

**Tool 2 — `generate_quiz_and_answers`**
- Input: Learning objectives from Tool 1
- Task: Create multiple-choice, true/false, and short-answer questions with explanations
- Output: A formatted quiz followed by a separate answer key

**System Prompt:** Act as a fair instructional designer. Always use Tool 1 before Tool 2 and ensure every answer is supported by the provided material.

---

### 20. Jolly Shringi — Recipe Adaptation Agent

**Email:** jollyshringi.888@gmaill.com  
**Python file:** `recipe_adaptation_agent.py`

**Use Case:** Adapt a recipe to dietary needs, ingredients, serving size, and cooking constraints.

**Tool 1 — `analyze_recipe_constraints`**
- Input: Original recipe, servings, restrictions, allergies, available ingredients, and equipment
- Task: Identify incompatible ingredients, substitutions, quantity changes, and cooking risks
- Output: A structured adaptation plan

**Tool 2 — `rewrite_adapted_recipe`**
- Input: Adaptation plan from Tool 1
- Task: Produce an updated ingredient list and numbered instructions with quantities and substitution notes
- Output: A complete adapted recipe in Markdown

**System Prompt:** Act as a safety-conscious home cooking assistant. Always use Tool 1 before Tool 2, treat allergies seriously, and never claim uncertain substitutions are allergen-safe.

---

## Evaluation Criteria

| Criteria | Points |
|---|---:|
| Code follows the same LangChain agent structure as `email_humanizer_agent.py` | 20 |
| Both tools are implemented correctly using `@tool` and `PromptTemplate` | 20 |
| Agent runs end-to-end without errors | 20 |
| `README.md` clearly explains the use case and how to run it | 20 |
| GitHub repository is public, clean, and includes `.env.example` without a real API key | 20 |
| **Total** | **100** |

---

## Tips

- Run the original `email_humanizer_agent.py` first to understand the flow.
- Read the reference repository's `README.md` and understand the think → act → observe loop.
- Add `.env` to `.gitignore`; never push your OpenAI API key.
- Test each tool separately before testing the complete agent.
- Use clear type hints and helpful tool docstrings.
- Tell the agent in `SYSTEM_PROMPT` to always call Tool 1 first and Tool 2 second.
- Test with at least three inputs and document one example in your `README.md`.

---

*Deadline and submission link: shared on WhatsApp. Post your public GitHub repository URL in the Excel sheet.*
