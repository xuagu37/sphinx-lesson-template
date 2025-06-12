# Mälardalen University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 3</p>


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

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Lecturer in English</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I018/1151/main?site=8&validator=2efd9e54ee423d53334ac7960e3b4e03&lang=UK&rmpage=job&rmjob=3194)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-05

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc in Higher Education Pedagogy</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I018/1151/main?site=8&validator=2efd9e54ee423d53334ac7960e3b4e03&lang=UK&rmpage=job&rmjob=3136)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-10

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Student Research Assistant-Bubble Barrier Project for River Plastics</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I018/1151/main?site=8&validator=2efd9e54ee423d53334ac7960e3b4e03&lang=UK&rmpage=job&rmjob=3233)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-06-25
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
