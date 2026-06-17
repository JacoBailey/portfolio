from app.database import SessionLocal
from app.models import Project, ProjectBullet, TechnicalSkill, TechnicalBullet, Experience, ExperienceBullet

db = SessionLocal()

def seed_projects():
    
    shredfinder = Project(
        name="ShredFinder",
        description="Snowboard recommendation web application that aggregates product data and reviews into a structured, searchable database.",
        bullets=[
            ProjectBullet(
                text="Product recommendation system using attribute-based scoring and ranking logic",
                order_index=1
            ),
            ProjectBullet(
                text="Relational database to normalize snowboard specs and review data",
                order_index=2
            ),
            ProjectBullet(
                text="API layer for querying and ranking snowboard matches",
                order_index=3
            )
        ]
    )

    portfolio = Project(
        name="Portfolio Website",
        description="Backend-driven portfolio that serves core webpages via a structured API and relational database.",
        bullets=[
            ProjectBullet(
                text="Built REST API using FastAPI to serve dynamic portfolio content",
                order_index=1
            ),
            ProjectBullet(
                text="Designed normalized PostgreSQL database schema with SQLAlchemy ORM models and relationships to support dynamic site content",
                order_index=2
            ),
            ProjectBullet(
                text="Implemented testing (Pytest), database migrations (Alembic), and structured logging to improve reliability and maintainability",
                order_index=3
            )
        ]
    )

    chatgpt_automation = Project(
        name="ChatGPT Automation",
        description="Automation tool for streamlining ChatGPT workflows using template-based prompt workflows and browser automation.",
        bullets=[
            ProjectBullet(
                text="Built regex-based template parser to dynamically inject user inputs into structured prompt templates",
                order_index=1
            ),
            ProjectBullet(
                text="Developed SeleniumBase automation layer to execute and stabilize browser-based interactions",
                order_index=2
            ),
            ProjectBullet(
                text="Designed custom template system enabling reusable workflows with input slot syntax",
                order_index=3
            ),
        ]
    )

    text_formatter = Project(
        name="Text Formatter",
        description="“Text Formatter” is a modular text-processing utility that provides multiple modes for transforming and formatting text-based string data.",
        bullets=[
            ProjectBullet(
                text="Designed modular architecture with isolated formatting modes to improve maintainability and extensibility",
                order_index=1
            ),
            ProjectBullet(
                text="Implemented list formatting utilities for applying prefixes and suffixes to structured data",
                order_index=2
            ),
            ProjectBullet(
                text="Designed custom template with input slots system to enable streamlined workflows",
                order_index=3
            ),
            ProjectBullet(
                text="Built regex-based transformation tooling for single and multi-step replacement workflows",
                order_index=4
            ),
        ]
    )

    projects = [shredfinder, portfolio, chatgpt_automation, text_formatter]

    db.add_all(projects)

def seed_technical_skills():
        
    languages = TechnicalSkill(
        name="Languages",
        bullets=[
            TechnicalBullet(
                text="Python",
                order_index=1
            ),
            TechnicalBullet(
                text="SQL",
                order_index=2
            ),
            TechnicalBullet(
                text="Javascript",
                order_index=3
            ),
            TechnicalBullet(
                text="HTML",
                order_index=4
            ),
            TechnicalBullet(
                text="CSS",
                order_index=5
            )
        ]
    )

    backend = TechnicalSkill(
        name="Backend",
        bullets=[
            TechnicalBullet(
                text="FastAPI",
                order_index=1
            ),
            TechnicalBullet(
                text="REST APIs",
                order_index=2
            ),
            TechnicalBullet(
                text="Microservices",
                order_index=3
            ),
            TechnicalBullet(
                text="API Development",
                order_index=4
            )
        ]
    )

    relational_databases = TechnicalSkill(
        name="Relational Databases",
        bullets=[
            TechnicalBullet(
                text="PostgreSQL",
                order_index=1
            ),
            TechnicalBullet(
                text="SQLAlchemy",
                order_index=2
            ),
            TechnicalBullet(
                text="Alembic",
                order_index=3
            ),
            TechnicalBullet(
                text="SQLAdmin",
                order_index=4
            )
        ]
    )

    testing = TechnicalSkill(
        name="Testing",
        bullets=[
            TechnicalBullet(
                text="Pytest",
                order_index=1
            )
        ]
    )

    devops = TechnicalSkill(
        name="DevOps",
        bullets=[
            TechnicalBullet(
                text="Docker",
                order_index=1
            ),
            TechnicalBullet(
                text="Docker Compose",
                order_index=2
            ),
            TechnicalBullet(
                text="Containerization",
                order_index=3
            )
        ]
    )

    tools = TechnicalSkill(
        name="Tools",
        bullets=[
            TechnicalBullet(
                text="Poetry",
                order_index=1
            ),
            TechnicalBullet(
                text="Loguru",
                order_index=2
            )
        ]
    )

    web_automation = TechnicalSkill(
        name="Web Automation",
        bullets=[
            TechnicalBullet(
                text="Selenium",
                order_index=1
            ),
            TechnicalBullet(
                text="SeleniumBase",
                order_index=2
            )
        ]
    )

    agile = TechnicalSkill(
        name="Agile",
        bullets=[
            TechnicalBullet(
                text="JIRA",
                order_index=1
            ),
            TechnicalBullet(
                text="Confluence",
                order_index=2
            ),
            TechnicalBullet(
                text="Kanban",
                order_index=3
            )
        ]
    )

    version_control = TechnicalSkill(
        name="Version Control",
        bullets=[
            TechnicalBullet(
                text="Git",
                order_index=1
            ),
            TechnicalBullet(
                text="GitHub",
                order_index=2
            )
        ]
    )

    additional = TechnicalSkill(
        name="Additional Skills",
        bullets=[
            TechnicalBullet(
                text="OOP",
                order_index=1
            ),
            TechnicalBullet(
                text="Regex",
                order_index=2
            )
        ]
    )

    technical_skills = [languages, backend, relational_databases, testing, devops, tools, web_automation, agile, version_control, additional]

    db.add_all(technical_skills)

def seed_experiences():
    
    torrid_technical_seo_analyst = Experience(
        role="Technical SEO Analyst",
        company="Torrid",
        start_date="October 2021",
        end_date="Present",
        bullets=[
            ExperienceBullet(
                text="Developed Python automation scripts to process repetitive LLM tasks and transform large text datasets, reducing repetitive manual work by 90%",
                order_index=1
            ),
            ExperienceBullet(
                text="Designed JSON schema structure in accordance with Schema.org documentation standards, fixing 40,000+ Google product and shopping errors",
                order_index=2
            ),
            ExperienceBullet(
                text="Collaborated in agile development workflows including sprint planning, grooming, and release validation",
                order_index=3
            ),
            ExperienceBullet(
                text="Designed and executed regular large-scale website crawls and specialized crawls for frontend data extraction (using site crawling tools by SEO Clarity and Screaming Frog SEO Spyder)",
                order_index=4
            ),
            ExperienceBullet(
                text="Created and managed 300+ front-end HTML/CSS content containers",
                order_index=5
            )
        ]
    )

    experiences = [torrid_technical_seo_analyst]

    db.add_all(experiences)

# If project is being run directly (not imported), execute seed functions
if __name__ == "__main__":
    seed_projects()
    seed_technical_skills()
    seed_experiences()
    db.commit()
    db.close()