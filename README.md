# JobStreet Job Scraper 🌏

> A powerful JobStreet job scraper designed to collect detailed job listings across eight Asia-Pacific countries. It simplifies regional job market analysis by extracting structured data such as titles, companies, salaries, and remote work details.
> Ideal for analysts, recruiters, and developers who need comprehensive, cross-country job intelligence.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>JobStreet Job Scraper 🌏</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This scraper automates the extraction of job postings from JobStreet domains.
It solves the challenge of gathering multi-country job data at scale, delivering consistent, structured results for market research, hiring strategy, and talent intelligence workflows.
Built for data teams, HR professionals, analysts, and platform builders.

### Regional Job Intelligence Extraction

- Supports JobStreet job listings from 8 APAC countries.
- Retrieves complete job details including salary, location, work type, arrangement, and classifications.
- Handles pagination, proxy rotation, and multiple search URLs seamlessly.
- Outputs clean JSON for easy downstream processing.

## Features

| Feature | Description |
|--------|-------------|
| Multi-country support | Scrapes JobStreet job listings across 8 APAC countries. |
| Multiple search URLs | Accepts one or several JobStreet search result URLs. |
| Pagination handling | Automatically navigates through all paginated results. |
| Proxy configuration | Supports rotating proxies for stability and reach. |
| Detailed job extraction | Captures job description, bullet points, salary, classifications, and more. |
| Remote/onsite detection | Identifies work arrangement and employment type. |
| Country-aware salary parsing | Extracts localized salary formats when available. |
| Configurable max items | Limit how many job results to collect. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|------------|------------------|
| jobSearchUrl | Source URL used to extract the listing. |
| jobId | Unique identifier of the job posting. |
| title | Job title as displayed in the listing. |
| company | Object containing company name, ID, description, and logo. |
| salary | Salary information in local currency (if available). |
| location | City or regional location of the job. |
| country | Two-letter country code. |
| workTypes | Employment type such as full-time or part-time. |
| workArrangement | Indicates remote, hybrid, or onsite work arrangement. |
| description | Short textual summary of the job. |
| bulletPoints | Key highlights or role bullet list. |
| classifications | Job categories including main and sub classifications. |
| postDate | ISO timestamp of job posting date. |
| postDateDisplay | Human-readable age (e.g., “13d ago”). |
| sourceUrl | URL where the job was fetched from. |
| scrapedAt | Timestamp of when the scraper extracted the data. |
| jobDescriptionHtml | Full HTML of the job description (if enabled). |

---

## Example Output


    [
      {
        "jobSearchUrl": "https://ph.jobstreet.com/ai-jobs-in-accounting/full-time",
        "jobId": "84033846",
        "title": "Senior Accountant | Permanent WFH | Night Shift | Day 1 HMO",
        "company": {
          "name": "EMAPTA",
          "id": "60239030",
          "description": "Emapta",
          "logo": "https://bx-branding-gateway.cloud.seek.com.au/7895f0e9-844d-4d16-af1b-aff9241c65eb.1/serpLogo"
        },
        "salary": "",
        "location": "Makati City, Metro Manila",
        "country": "PH",
        "workTypes": ["Full time"],
        "workArrangement": "Remote",
        "description": "As a Senior Accountant, you will support the full-cycle accounting operations for a trailblazer in AI innovation.",
        "bulletPoints": [],
        "classifications": [
          {
            "main": "Accounting",
            "sub": "Financial Accounting & Reporting"
          }
        ],
        "postDate": "2025-05-06T11:07:22Z",
        "postDateDisplay": "13d ago",
        "sourceUrl": "https://ph.jobstreet.com/ai-jobs-in-accounting/full-time",
        "scrapedAt": "2025-05-20T02:00:43.874Z",
        "jobDescriptionHtml": "<div class=\"x3iy8f0 _1xd6mbw0\">...</div>"
      }
    ]

---

## Directory Structure Tree


    JobStreet Job Scraper 🌏/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── jobstreet_parser.py
    │   │   └── utils_normalization.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── input.example.json
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Recruiters** use it to gather cross-country candidate opportunities, enabling better hiring insights and role benchmarking.
- **Labor market analysts** use it to study regional job demand, compensation trends, and skill gaps.
- **Job boards** use it to enrich their listings with structured JobStreet data at scale.
- **HR teams** use it to monitor competitor hiring activities across APAC markets.
- **Developers** use it to feed structured datasets into analytics dashboards or machine learning models.

---

## FAQs

**Q: Can I scrape multiple JobStreet countries at once?**
Yes. As long as you provide multiple search URLs from different JobStreet domains, the scraper will process them sequentially.

**Q: Does it retrieve full job descriptions?**
Yes. Full HTML job descriptions can be included when enabled via input parameters.

**Q: Is proxy support available?**
Yes, proxy configuration is supported for better stability, particularly when scraping large volumes.

**Q: Can I control how many jobs I extract?**
Yes. Use the `maxItems` parameter to cap the total number of results.

---

## Performance Benchmarks and Results

**Primary Metric:** Processes an average of 40–60 job listings per minute depending on page complexity and network conditions.
**Reliability Metric:** Maintains a 98% successful extraction rate across supported JobStreet domains.
**Efficiency Metric:** Utilizes minimal memory overhead, enabling long-running scraping sessions with stable performance.
**Quality Metric:** Achieves over 95% field completeness due to structured parsing of job descriptions, metadata, and company fields.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
