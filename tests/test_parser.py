from swedjobs.parser import parse_jobs_lund, parse_jobs_uppsala, parse_jobs_stockholm, parse_jobs_gothenburg, parse_jobs_ki, parse_jobs_kth, parse_jobs_linkoping, parse_jobs_umea

def test_parser():
    test_file = "html_cache/latest_umea_page.html"
    jobs = parse_jobs_umea(test_file)

    print(f"\nTest complete: {len(jobs)} job(s) found.\n")

    for i, job in enumerate(jobs, 1):
        print(f"--- Job {i} ---")
        print(f"Title     : {job['title']}")
        print(f"URL       : {job['url']}")
        print(f"Department: {job['department']}")
        print(f"Published : {job['published']}")
        print(f"Deadline  : {job['deadline']}\n")

if __name__ == "__main__":
    test_parser()
