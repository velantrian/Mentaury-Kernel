# 🪁 Mentaury-Kernel

> **Технологически нейтральная спецификация композиции для безопасного семантического взаимодействия между 🧬 Velantrim Native Kernel и 🌀 Mentaury Soul.**

Mentaury-Kernel определяет **правила композиции**, а не создаёт третью когнитивную систему. Его задача — сохранять смысл, provenance, неопределённость, scope, явно объявленные потери, identity attribution и границы полномочий, когда информация пересекает независимо управляемые домены.

[🇬🇧 English version](README.md)

## 📌 Статус

- **Document envelope:** `DRAFT v0.2.4 · DOCUMENT_RECONCILIATION_ONLY`
- **Semantic architecture baseline:** `v0.2.3`
- **Стадия репозитория:** `SPECIFICATION_BOOTSTRAP_ONLY`
- **Архитектура:** `ARCHITECTURE_ONLY · TECHNOLOGY_NEUTRAL`
- **Runtime-код:** `NONE`
- **Cognition runtime:** `NONE`
- **Truth / identity / action authority:** `NONE`
- **Production authority:** `NONE`

`v0.2.4 ≠ новый semantic Canon`

### 🧭 Authority документации на этапе bootstrap

Постоянная модель authority между Notion и GitHub всё ещё **OPEN** в [Issue #2](https://github.com/velantrian/Mentaury-Kernel/issues/2). Само создание репозитория и merge документации **не делают GitHub semantic Canon автоматически**.

Если GitHub и исходная Notion-архитектура расходятся, нельзя молча выбрать одну поверхность: нужно остановиться и выполнить явную reconciliation по [`docs/CURRENT_STATUS.md`](docs/CURRENT_STATUS.md).

## 🧭 Основная граница

```text
🧬 Velantrim Native Kernel
        │
        │ versioned meaning / continuity material
        ▼
🌉 Semantic Continuity Port
        │
        ▼
🌀 Mentaury Soul

🪁 Mentaury-Kernel
= composition invariants
≠ cognition
≠ truth authority
≠ identity authority
≠ runtime coordinator
```

### Базовые законы

```text
COMPOSITION ≠ COGNITION
INTEGRATION ≠ AUTHORITY TRANSFER
REPRESENTATION ≠ REALITY / TRUTH
TRANSPORT SUCCESS ≠ SEMANTIC APPROVAL
DELIVERED ≠ TRUE ≠ IDENTITY_ADMITTED
SHARED HISTORY ≠ SAME CURRENT IDENTITY
RECORD MERGE ≠ IDENTITY MERGE
SOURCE UPDATE ≠ AUTOMATIC COMPOSITION UPDATE
```

## ⚖️ Владение доменами

| Контур | Владеет | Не владеет |
|---|---|---|
| 🧬 **Velantrim Native Kernel** | epistemic-history semantics: provenance, uncertainty, accountable revision / retention / loss | cognition, identity admission, relationship truth |
| 🌀 **Mentaury Soul** | cognition-domain и identity-domain semantics | переписыванием upstream provenance или автоматическим повышением claim до truth |
| 🌉 **Continuity Port** | transport, version / compatibility checks, structural validation, declared loss, bounded receipts | truth, identity, consent, action decisions |
| 🪁 **Mentaury-Kernel** | composition invariants, authority boundaries, cross-system threat model, conformance specification | внутренними алгоритмами, superior authority, runtime coordination |
| 🏛️ **Governance** | bounded authorization / admission procedures соответствующего проекта | автоматической truth- или identity-content authority |

## 🧬 Технологическая нейтральность

Mentaury-Kernel намеренно **не привязан** к конкретному вычислительному субстрату или современному AI-стеку.

Он не требует и не канонизирует:

- конкретную LLM или семейство моделей;
- prompts или механику context window;
- embeddings или vector database;
- graph database;
- RAG;
- конкретный язык программирования;
- конкретный storage engine;
- agent framework;
- конкретное устройство или среду выполнения.

Будущая реализация может использовать такие технологии, но они остаются **implementation profiles**, а не Canon Mentaury-Kernel.

## 🚫 Что не является целью

Mentaury-Kernel — это **не**:

- третий production-runtime;
- Cognition Engine;
- Identity Engine;
- Truth Gate;
- autonomous loop или scheduler;
- архитектура базы данных или graph;
- зеркало live GitHub / CI статуса соседних проектов;
- утверждение о сознании, жизни, sentience или AGI.

## 🔬 Дисциплина включения

Новый invariant может войти сюда только если одновременно:

1. он относится к **cross-domain composition**;
2. без него существует конкретный semantic / authority / provenance / scope / loss failure;
3. существующие invariants этот failure не покрывают;
4. правило можно выразить минимальной technology-neutral границей;
5. оно не описывает внутреннее cognition Mentaury Soul или внутренний epistemic-history mechanism Native Kernel.

```text
ARCHITECTURAL FIT ≠ ARCHITECTURAL NECESSITY
IMPORTANT IDEA ≠ MENTAURY-KERNEL RESPONSIBILITY
```

## 📚 Структура репозитория

```text
README.md
README.ru.md

docs/
├── CURRENT_STATUS.md
├── ARCHITECTURE.md
├── PROVENANCE_MATRIX.md
├── COMPOSITION_INVARIANTS.md
├── THREAT_MODEL.md
├── CONFORMANCE_SCENARIOS.md
└── AI_CONTEXT.md

.github/
└── pull_request_template.md
```

## 🚦 Текущая инженерная граница

Этот репозиторий создаётся прежде всего как **specification repository**. Сначала здесь фиксируются документация, conformance definitions, provenance records и governance boundaries.

Сам факт создания репозитория **не** разрешает runtime implementation, wire protocol, выбор базы данных, model integration, executable autonomy или production deployment.

Перед любым изменением см. [`docs/CURRENT_STATUS.md`](docs/CURRENT_STATUS.md).

---

### 🏁 North Star

> Mentaury-Kernel не создаёт интеллект, identity или truth. Он определяет условия, при которых независимо управляемые системы могут обмениваться смыслом без молчаливой потери provenance, uncertainty, semantic distinctions и authority boundaries.
