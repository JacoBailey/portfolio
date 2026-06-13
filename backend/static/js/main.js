// -----------------
// PROJECTS
// -----------------

// Fetch skills from API

async function fetchProjects() {
  const res = await fetch("/api/projects/");
  
  if (!res.ok) throw new Error("Failed to fetch projects");
  
  return await res.json();

}

// Render projects + nested bullets

function renderProjects(projects) {
  const container = document.getElementById("projects-container");
  
  container.innerHTML = projects.map(project => `
    <div class="project-block">
        <h3 class="project-name">${project.name}</h3>
        <div class="project-description">${project.description}</div>
        <ul class="project-bullets-container">${project.bullets
            .sort((a,b) => a.order_index - b.order_index)
            .map(bullet => `<li class="project-bullet">${bullet.text}</li>`)
            .join("")
        }</ul> 
    </div>
    `).join("");
}

// Init

async function initProjects() {
  try {
    const projects = await fetchProjects();
    renderProjects(projects);
  }
  
  catch (err) {
    console.error("Projects load error:", err);
  }
}


// -----------------
// TECHNICAL SKILLS
// -----------------

// Fetch skills from API

async function fetchSkills() {
  const res = await fetch("/api/skills/");
  
  if (!res.ok) throw new Error("Failed to fetch skills");
  
  return await res.json();

}

// Render skills + nested bullets

function renderSkills(skills) {
  const container = document.getElementById("skills-container");
  
  container.innerHTML = skills.map(skill => `
    <div class="skill-block">
      <span class="skill-name">${skill.name}: </span>
      <span class="skill-bullets">
        ${skill.bullets
          .sort((a, b) => a.order_index - b.order_index)
          .map(bullet => bullet.text)
          .join(", ")
        }
      </span>
    </div>
  `).join("");
}

// Init

async function initSkills() {
  try {
    const skills = await fetchSkills();
    renderSkills(skills);
  }
  
  catch (err) {
    console.error("Skills load error:", err);
  }
}


// -----------------
// EXPERIENCE
// -----------------

// Fetch experience from API

async function fetchExperience() {
  const res = await fetch("/api/experience/");
  
  if (!res.ok) throw new Error("Failed to fetch experience");
  
  return await res.json();

}

// Render experience + nested bullets

function renderExperience(experiences) {
  const container = document.getElementById("experience-container");
  
  container.innerHTML = experiences.map(experience => `
        <div class="experience-block">
            <h3 class="experience-role">${experience.role}</h3>
            <div class="experience-company">${experience.company}</div>
            <div class="experience-daterange">${experience.start_date} - ${experience.end_date}</div>
            <ul class="experience-bullets-container">${experience.bullets
                .sort((a, b) => a.order_index - b.order_index)
                .map(bullet => `<li class="experience-bullet">${bullet.text}</li>`)
                .join("")
            }</ul>
        </div>
  `).join("");
}

// Init

async function initExperience() {
  try {
    const experience = await fetchExperience();
    renderExperience(experience);
  }
  
  catch (err) {
    console.error("Experience load error:", err);
  }
}


// ------------
// Run scripts
// ------------

document.addEventListener("DOMContentLoaded", () => {
    initProjects();
    initSkills();
    initExperience();
});