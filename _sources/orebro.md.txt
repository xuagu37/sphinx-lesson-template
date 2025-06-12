# Örebro University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 9</p>


<div id="filters" style="margin: 1em 0;">
  <label for="filterType"><strong>Filter by Job Type:</strong></label>
  <select id="filterType" style="margin-right: 1em;">
    <option value="">Show All</option>
    <option value="PhD">PhD</option>
    <option value="Postdoc/Researcher">Postdoc/Researcher</option>
    <option value="Lecturer/Professor">Lecturer/Professor</option>
    <option value="Research Engineer">Research Engineer</option>    
    <option value="Other">Other</option>
  </select>
  <input type="text" id="jobFilter" placeholder="Search jobs..." style="padding: 0.5em; width: 50%;">
</div>

<div id="jobList">
<div class="job" data-type="None" style="margin-bottom: 1.5em;">

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Laboratory assistant in Biomedicine/Toxicology</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250201)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-06-19

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researchers in Computer Science, Cybersecurity</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250159)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-06-23

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researchers in Computer Science, Cybersecurity and Embodied AI</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250160)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-06-23

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in Economics</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250205)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-07-31

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral students in Computer Science, Cybersecurity</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250141)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-07-31

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral students in Computer Science, Cybersecurity and Embodied AI</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250142)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-07-31

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Associate senior lecturer in Computer Science, Cybersecurity</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250158)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-07-31

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researcher in criminology</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250199)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-11

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researcher in Biomedicine/Toxicology</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250172)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-11
</div></div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const typeSelect = document.getElementById('filterType');
  const textInput = document.getElementById('jobFilter');
  const jobBlocks = document.querySelectorAll('.job');

  function updateDisplay() {
    const selected = typeSelect.value.toLowerCase();
    const query = textInput.value.toLowerCase();

    jobBlocks.forEach(job => {
      const jobType = (job.dataset.type || "").toLowerCase();
      const matchesType = !selected || jobType === selected;
      const matchesQuery = job.textContent.toLowerCase().includes(query);
      job.style.display = (matchesType && matchesQuery) ? '' : 'none';
    });
  }

  typeSelect.addEventListener('change', updateDisplay);
  textInput.addEventListener('input', updateDisplay);
});
</script>
