# 🏗️ From QA Bot to Task Agent: An Architecture Guide

> **TL;DR:** Stop building chatbots that just answer questions. Start building **Task Agents** that actually *do work*.  
> This guide explains the architectural shift from monolithic QA bots to **Task Agents** using **Static Rules**, **Dynamic Skills**, and **Deterministic Hooks**—with concrete code examples and open-source references.

---

## 1. The Core Shift: QA Bot → Task Agent

Most AI systems today are still **context-stuffed QA bots**:
- They answer questions well
- They hallucinate under pressure
- They lack guarantees around execution, safety, and consistency

A **Task Agent** is different. It is designed to **execute tasks reliably**, not just talk.

The key insight:

> **Don’t scale context. Structure it.**

We split agent intelligence into **three layers**.

---

## 2. The Three-Layer Architecture

### 🧱 1. Static Context — Rules (Always On)

**Mental model:** *Employee handbook*

- Always loaded
- Defines identity, coding standards, behavioral constraints
- Prevents hallucinations and style drift
- Small, stable, human-editable

**Storage**
- Markdown files (e.g. `.cursorrules`)
- Repo-local, version-controlled

---

### 🛠️ 2. Dynamic Context — Skills (On Demand)

**Mental model:** *Toolbox*

- Loaded only when needed
- Each skill is a self-contained capability
- Keeps the context window clean

**Storage**
- MCP (Model Context Protocol) servers
- Tool definitions

---

### ⚓ 3. Deterministic Hooks — Guardrails

**Mental model:** *Security + Compliance layer*

- Not probabilistic
- Runs before / after LLM reasoning
- Enforces rules that must never fail

---

## 3. Recommended Project Structure

```
my-task-agent/
├── .cursorrules
├── main.py
├── tools/
│   └── linear_mcp.py
└── README.md
```

---

## 4. Static Context Example: `.cursorrules`

```markdown
# ROLE
You are a Senior Python Engineer focused on production-grade systems.

# RULES
- NEVER use print() for debugging
- ALWAYS type-hint functions
- Propose a plan if touching >3 files

# BEHAVIOR
- Be concise
- Ask clarifying questions if needed
```

Reference:
https://github.com/PatrickJS/awesome-cursorrules

---

## 5. Dynamic Skill Example (MCP)

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DevTools")

@mcp.tool()
def create_linear_ticket(title: str, priority: str = "low") -> str:
    ticket_id = f"LIN-{hash(title) % 10000}"
    return f"Created ticket {ticket_id} with priority={priority}"

if __name__ == "__main__":
    mcp.run()
```

Reference:
https://github.com/modelcontextprotocol/python-sdk

---

## 6. Deterministic Hook Example

```python
def compliance_check_hook(state):
    user_input = state["messages"][-1].content.lower()
    if "password" in user_input or "api_key" in user_input:
        return {"error": "Security violation detected"}
    return agent_node(state)
```

Reference:
https://langchain-ai.github.io/langgraph/

---

## Final Thought

If your agent only answers questions, it’s a chatbot.  
If it reliably executes work, it’s a **Task Agent**.
