# -*- coding: utf-8 -*-
"""
Site content. Edit this file, then run:  python3 build.py

Anything left as "" (empty) is simply not shown on the site.
"""

SITE = {
    # GitHub Pages address (repository: github.com/tsy2i/tsy2i.github.io)
    "base_url": "https://tsy2i.github.io",
    "name": "Sungyoon Lee",
    "title": "Associate Professor of Literacy Education",
    "affiliation": "Department of Teaching, Learning, and Innovation",
    "institution": "Middle Tennessee State University",
    "location": "Murfreesboro, Tennessee, USA",
    "institution_url": "https://www.mtsu.edu/",
    "email": "Sungyoon.Lee@mtsu.edu",
    "cv_file": "",  # e.g. "CV.pdf" to link a CV again
    "tagline": "Reading, writing and literacy research",
    "bio": (
        "Sungyoon Lee is a literacy researcher whose work examines how children and adolescents "
        "read, write and learn from texts. The work spans eye-tracking studies of reading "
        "processes, the comprehension of illustrated science texts, early writing development, "
        "technology-supported literacy instruction, and meta-analyses of reading, writing and "
        "content-area interventions. Before doctoral study at Texas A&amp;M University (Ph.D. 2019), "
        "Sungyoon Lee taught for about a decade in elementary schools in Seoul, South Korea."
    ),
    "knows_about": [
        "reading comprehension", "eye tracking in reading", "illustrated science texts",
        "writing development", "meta-analysis", "technology-integrated literacy instruction",
        "English language learners", "teacher education",
    ],
    # Fill in whichever profiles you have; empty ones are hidden.
    "profiles": [
        ("ORCID 0000-0002-3326-1966", "https://orcid.org/0000-0002-3326-1966"),
        ("Google Scholar", "https://scholar.google.com/citations?user=fuhQSEMAAAAJ"),
        ("MTSU faculty page", "https://w1.mtsu.edu/faculty/sungyoon-lee"),
        ("ResearchGate", ""),
        ("LinkedIn", ""),
    ],
    "honour": "Recipient of the 2024 Womack College Research Award, Middle Tennessee State University.",
}

# Topic groups shown on the home page, in order. (section, topic_id, label)
TOPICS = [
    ("Research areas", "reading", "Reading processes, comprehension and eye tracking"),
    ("Research areas", "writing", "Early writing and literacy development"),
    ("Research areas", "technology", "Technology and online learning"),
    ("Research areas", "context", "Students, teachers and school contexts"),
    ("Research methods", "meta", "Meta-analysis and research synthesis"),
    ("Research methods", "methods", "Eye tracking, qualitative and review methods"),
]

# oa: "oa" = free on publisher's site, "green" = free copy elsewhere, "" = unknown/none
# summary / keywords: optional; when present the paper page shows them.
PUBLICATIONS = [
    dict(slug="covid19-students-with-disabilities-2026", year=2026,
         authors="Montague, M. L., Ducy, E., Lee, S., Sweet, K., Lynch, P. S., Miracle, I., Beard, A. S., & Stough, L. M.",
         title="The COVID-19 pandemic's impact on the education of students with disabilities: Multiple perspectives on the “weird normal”",
         journal="Journal of the American Academy of Special Education Professionals", volume="21", issue="2", pages="47-62",
         doi="10.64546/jaasep.642", oa="", topics=["context"]),
    dict(slug="preschool-oral-storytelling-visual-design-2026", year=2026,
         authors="FitzPatrick, E., Schrodt, K., Davis, T., Lee, S., & Towson, J.",
         title="Foundations for writing: Preschool oral storytelling following visual design and grammar instruction",
         journal="Reading and Writing: An Interdisciplinary Journal", volume="", issue="", pages="",
         doi="10.1007/s11145-026-10817-1", oa="", topics=["writing"]),
    dict(slug="social-studies-interventions-meta-analysis-2026", year=2026,
         authors="Lee, S., Williams, M., Rice, M., & Wijekumar, K.",
         title="A meta-analysis of social studies interventions on secondary students' learning",
         journal="Review of Educational Research", volume="", issue="", pages="",
         doi="10.3102/00346543261418046", oa="", topics=["meta"]),
    dict(slug="teaching-social-presence-digital-literacy-2026", year=2026,
         authors="Lee, S., Hwang, H., Shin, Y., & Kendeou, P.",
         title="Teaching presence, social presence, and digital literacy in predicting online learning experience in elementary students",
         journal="British Journal of Educational Technology", volume="57", issue="1", pages="185-203",
         doi="10.1111/bjet.70004", oa="", topics=["technology"]),
    dict(slug="teacher-student-relationships-engagement-2025", year=2025,
         authors="Kang, D., Lee, S., Shi, Q., & Jia, Y.",
         title="Longitudinal associations between teacher-student relationships and school engagement in early elementary school years: Gender differences",
         journal="Applied Developmental Science", volume="", issue="", pages="",
         doi="10.1080/10888691.2025.2458624", oa="", topics=["context"]),
    dict(slug="invented-spelling-writing-motivation-2024", year=2024,
         authors="Schrodt, K., FitzPatrick, E., Lee, S., McKeown, D., McColloch, A., & Evert, K.",
         title="The effects of invented spelling instruction on literacy achievement and writing motivation",
         journal="Education Sciences", volume="14", issue="9", pages="1020", article=True,
         doi="10.3390/educsci14091020", oa="oa", topics=["writing"]),
    dict(slug="motivational-resilience-teacher-support-2024", year=2024,
         authors="Kang, D., Lee, S., & Liew, J.",
         title="Academic motivational resilience and teacher support: Academic self-efficacy as a mediator",
         journal="European Journal of Psychology of Education", volume="39", issue="", pages="4417-4435",
         doi="10.1007/s10212-024-00870-1", oa="", topics=["context"]),
    dict(slug="picturebook-illustrations-preschool-narrative-2024", year=2024,
         authors="Davis, T., Schrodt, K., & Lee, S.",
         title="An exploration of the impact of quality illustrations in children's picturebooks on preschool student narrative ability",
         journal="Reading Psychology", volume="45", issue="7", pages="639-661",
         doi="10.1080/02702711.2024.2351480", oa="", topics=["writing", "reading"]),
    dict(slug="spatial-ability-illustrated-science-texts-eye-tracking-2023", year=2023,
         authors="Lee, S.",
         title="The role of spatial ability and attention shifting in reading of illustrated scientific texts: An eye tracking study",
         journal="Reading Psychology", volume="44", issue="8", pages="915-935",
         doi="10.1080/02702711.2023.2202186", oa="", topics=["reading", "methods"]),
    dict(slug="technology-ell-literacy-meta-analysis-2022", year=2022,
         authors="Lee, S., Kuo, L.-J., Xu, Z., & Hu, X.",
         title="The effects of technology-integrated classroom instruction on English language learners' literacy development: A meta-analysis",
         journal="Computer Assisted Language Learning", volume="35", issue="5-6", pages="1106-1137",
         doi="10.1080/09588221.2020.1774612", oa="", topics=["technology", "meta"]),
    dict(slug="reading-skills-eye-movements-silent-reading-2022", year=2022,
         authors="Lee, S., Woltering, S., Prickett, C., Linda, H., Shi, Q., & Thompson, J.",
         title="Exploring the associations between reading skills and eye movements in elementary children's silent sentence reading",
         journal="Reading Psychology", volume="43", issue="1", pages="85-103",
         doi="10.1080/02702711.2021.2020189", oa="", topics=["reading", "methods"]),
    dict(slug="grounded-theory-educational-research-2021", year=2021,
         authors="Stough, L. M., & Lee, S.",
         title="Grounded theory approaches used in educational research journals",
         journal="International Journal of Qualitative Methods", volume="20", issue="", pages="",
         doi="10.1177/16094069211052203", oa="oa", topics=["methods"]),
    dict(slug="disasters-schools-children-disability-2020", year=2020,
         authors="Stough, L. M., Ducy, E., Kang, D., & Lee, S.",
         title="Disasters, schools, and children: Disability at the intersection",
         journal="International Journal of Disaster Risk Reduction", volume="45", issue="", pages="101447", article=True,
         doi="10.1016/j.ijdrr.2019.101447", oa="", topics=["context"]),
    dict(slug="vocabulary-instruction-critical-analysis-2018", year=2018,
         authors="Moody, S. M., Hu, X., Kuo, L.-J., Jouhar, M., Xu, Z., & Lee, S.",
         title="Vocabulary instruction: A critical analysis of theories, research, and practice",
         journal="Education Sciences", volume="8", issue="4", pages="180", article=True,
         doi="10.3390/educsci8040180", oa="oa", topics=["reading", "meta"]),
    dict(slug="seven-school-related-disasters-2018", year=2018,
         authors="Stough, L. M., Kang, D., & Lee, S.",
         title="Seven school-related disasters: Lessons for policymakers and school personnel",
         journal="Education Policy Analysis Archives", volume="26", issue="", pages="100", article=True,
         doi="10.14507/epaa.26.3698", oa="oa", topics=["context"]),
    dict(slug="currere-and-prolepsis-2017", year=2017,
         authors="Hall, K., Suárez, M. I., Lee, S., & Slattery, P.",
         title="Currere and prolepsis: A literary analysis",
         journal="The Currere Exchange Journal", volume="1", issue="1", pages="101-110",
         doi="", oa="", topics=["context"]),
    dict(slug="ies-funded-reading-research-review-2017", year=2017,
         authors="Lee, S., Kuo, L.-J., Moody, S. M., & Chen, Z.",
         title="Reviews of research funded by U.S. Institute of Educational Sciences: A case of reading development and instruction",
         journal="Cogent Education", volume="4", issue="1", pages="1401444", article=True,
         doi="10.1080/2331186x.2017.1401444", oa="oa", topics=["reading", "meta"]),
]

# Conference presentations: (authors, date, title, venue)
PRESENTATIONS = [
    ("DaSilva, A., Fields, S., Cao, Y., Lee, S., Ahn, P., & LePore, M.", "2026, July", "A meta-analysis of AI-integrated interventions for K-12 EFL learners across reading, writing, listening, and speaking domains", "Society for the Scientific Study of Reading, Rotterdam, Netherlands"),
    ("McDonell, L., DaSilva, A., Cuadron, M., Miller, K., & Lee, S.", "2026, July", "The effects of prior knowledge activation on college students' history text processing and comprehension", "Society for the Scientific Study of Reading, Rotterdam, Netherlands"),
    ("Lee, S., McClain, J., & Schrodt, K.", "2025, December", "Kindergarten writing motivation: From paper to iPad assessment", "Literacy Research Association, Las Vegas, NV"),
    ("Lee, S., Williams, M., Rice, M., & Wijekumar, K.", "2025, April", "A meta-analytic review of social studies interventions on secondary students' learning", "American Educational Research Association, Denver, CO"),
    ("Davis, T., McClain, J. B., Lee, S., & Schrodt, K.", "2024, July", "Designing early writing assessment: Impact of quality picture book study on preschool students' narrative storytelling and drawing", "Society for the Scientific Study of Reading, Copenhagen, Denmark"),
    ("Fields, S., McClain, J. B., DaSilva, A., Lee, S., & Barnes, Z. T.", "2024, July", "A meta-analysis of writing intervention studies for K-12 English Learners", "Society for the Scientific Study of Reading, Copenhagen, Denmark"),
    ("Kang, D., Lee, S., Shi, Q., & Jia, Y.", "2024, April", "Longitudinal associations between teacher-student relationships and school engagement in early elementary school years: Gender differences", "American Educational Research Association, Philadelphia, PA"),
    ("Lee, S., Hwang, H., & Shin, Y.", "2023, December", "The relationships among teaching presence, social presence, and digital literacy in elementary students' online learning self-efficacy", "Literacy Research Association, Atlanta, GA"),
    ("Lee, S.", "2023, July", "The role of spatial ability and attention shifting on the reading of illustrated scientific texts: An eye-tracking study", "Society for the Scientific Study of Reading, Port Douglas, Australia"),
    ("Schrodt, K., Lee, S., Adejumo, T., & FitzPatrick, E.", "2023, July", "The effects of invented spelling instruction on literacy achievement and writing motivation", "Society for the Scientific Study of Reading, Port Douglas, Australia"),
    ("Lee, S.", "2021, December", "Fourth and fifth grade students' reading of illustrated science texts", "Literacy Research Association, Atlanta, GA"),
    ("Lee, S.", "2020, July", "The role of working memory in integrative reading of text and picture", "Society for Text and Discourse, Atlanta, GA"),
    ("Lee, S., Prickett, C., Shi, Q., Sun, H., Thompson, J., & Woltering, S.", "2020, April", "The effects of oral reading fluency on student's reading behaviors in silent sentence processing: An eye-tracking study", "American Educational Research Association, San Francisco, CA"),
    ("Lee, S., Prickett, C., Shi, Q., Sun, H., Thompson, J., & Woltering, S.", "2019, April", "The relationship between eye movements and reading skills in elementary school children: An exploratory study", "American Educational Research Association, Toronto, Canada"),
    ("Stough, L. M., & Lee, S.", "2019, February", "An examination of grounded theory methods used in top ranked education journals", "Southwest Educational Research Association, San Antonio, TX"),
    ("Stough, L. M., Kang, D. H., & Lee, S.", "2018, July", "Seven school-related disasters: A multiple case study analysis", "Natural Hazards Workshop, Broomfield, CO (poster)"),
    ("Lee, S., Hu, X., Xu, Z., & Kuo, L.-J.", "2018, April", "Effects of educational technology on English language learners' literacy development: A meta-analysis", "American Educational Research Association, New York, NY"),
    ("Lee, S., & Kang, D. H.", "2018, April", "Effects of learner-generated drawing strategy on reading a science text: A meta-analysis", "American Educational Research Association, New York, NY (poster)"),
    ("Stough, L. M., Kang, D. H., & Lee, S.", "2018, February", "Disasters in school: Implications for teachers", "Southwest Educational Research Association, New Orleans, LA"),
    ("Kuo, L.-J., Lee, S., Kim, H., & Liu, M.", "2017, November", "Integrating STEM with world language instruction through project-based activities", "NFLC STARTALK Fall Conference, Portland, OR"),
    ("Lee, S., & Sim, J.-H.", "2017, October", "Aesthetic cultivation through knowledge acquisition: A new interpretation of Kant's Critiques", "Bergamo Conference on Curriculum Theory and Classroom Practice, Dayton, OH"),
    ("Hall, K., Slattery, P., Lee, S., & Suarez, M. I.", "2017, May", "Reading Moby Dick from the borderlands", "American Educational Research Association, San Antonio, TX"),
    ("Kuo, L.-J., Lee, S., Yang, X., Park, J. H., Choi, Y., Wang, A., Eslami, Z., & Keelen, A.", "2017, April", "The impact of biliteracy experience on visual processing", "Society for Research in Child Development, Austin, TX (poster)"),
    ("Lee, S., Kuo, L.-J., Chen, G. Z., Wang, A., Guo, D., Moon, C. Y., Park, J. H., Schluens, A., Dobson, J., & Ging, A. B.", "2016, December", "Reading research and trends: Reviews of federally-funded research and major synthesis", "Literacy Research Association, Nashville, TN"),
    ("Kuo, L.-J., Lee, S., Xie, W., & Han, F.", "2016, October", "Integrating STEM with world language instruction through student-centered activities", "NFLC STARTALK Fall Conference, Atlanta, GA"),
    ("Hall, K., Lee, S., Suarez, M. I., & Slattery, P.", "2016, October", "Reading Moby Dick from the borderlands", "Curriculum & Pedagogy Conference, Cleveland, OH"),
    ("Lee, S.", "2015, October", "Imagination in teacher education", "Bergamo Conference on Curriculum Theory and Classroom Practice, Dayton, OH"),
    ("Hall, K., Slattery, P., Lee, S., & Suárez, M. I.", "2015, May", "Reading Moby Dick from the borderlands", "SSGA El Mundo Zurdo Conference, University of Texas at Austin"),
]
