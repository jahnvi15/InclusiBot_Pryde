train_data = [
    ("Transitioning Tips", "What are some tips for transitioning and presenting as more feminine later in life?"),
    ("Sex after Surgery", "When can a person have sex after gender-affirming surgery?"),
    ("Achieve Orgasm", "Will it be possible to achieve orgasm after gender-affirming surgery?"),
    ("Desire to have sex", "How will gender-affirming surgery affect libido?"),
    ("vaginal depth after vaginoplasty",
     "What is the average vaginal depth after vaginoplasty?"),
    ("Aftercare for vaginoplasty", "What is the aftercare required after vaginoplasty?"),
    ("STI Protection after surgery",
     "How can one protect against STIs after gender-affirming surgery?"),
    ("Hygiene tips after vaginoplasty",
     "What hygiene tips are important after vaginoplasty?"),
    ("Vaginoplasty", "What is vaginoplasty?"),
    ("Vaginoplasty procedure", "How many stages are included in the procedure?"),
    ("Time during Vaginoplasty", "How long is vaginoplasty surgery?"),
    ("PrEP", "What is PrEP"),
    ("Hormones with PrEP", "Can you take hormones and PrEP or PEP?"),
    ("Getting PrEP", "Is PrEP right for you"),
    ("Sexual Health Tests",
     "Which tests are recommended to help ensure the sexual health of gay and bisexual men?"),
    ("Transgender sexual and reproductive health care",
     "Where can sexual and reproductive health providers find clinical guidelines for transgender people?"),
    ("Prevent Sexually Transmitted Diseases",
     "How You Can Prevent Sexually Transmitted Diseases"),
    ("HIV Test for Bisexual men", "How often should I get tested for HIV as a bisexual men?"),
    ("Heath Issures in Bisexual men",
     "What are health issues in Gay and Bisexual Men"),
    ("Heath Issures in Lesbian and Bisexual ",
     "What are heath Issures in Lesbian and Bisexual "),
    ("Pap Test", "Elaborate more on pap Test "),
    ("Protection from STD ", "How can you protect yourself from STDs?"),
    ("Most Common STD", "What are most common STD?"),
    ("STD", "What are STD ?"),
    ("HIV", "What is HIV?"),
    ("Sexual Health Tests in Bisexual men",
     "Which tests do I get for good sexual Health as a gay or bisexual men?"),
    ("Sexual Health Tests in Bisexual men",
     "Which test do I get as a bisexual men for good sexual health?"),
     ("Resources for LGBTQ+ Youth", "Can you suggest some resources for LGBTQ+ Youth"),
("Reseources for LGBT health", "Give some resources related to LGBT health"),
]
health_database = [
    ("flu", "The symptoms of the flu include fever, cough, sore throat, body aches, and fatigue. (Source: CDC)"),
    ("Vaginal depth and lubrication after surgery",
     "Vaginal depth varies but an average depth after vaginoplasty is 4-6 inches. Lubricants are needed for sex. \n (Source: Medical News Today, Medically reviewed by Francis Kuehnle)"),
    ("Transitioning", "Here are some tips to consider:\n\nNonmedical transitioning: Social transitioning can involve changing your name, asking others to use your preferred pronouns, and altering your appearance through wardrobe choices, makeup, hairstyle, or using prosthetics like hip pads or prosthetic breasts.\n\nMedical transitioning: Some individuals may choose to undergo medical treatments, such as hormone therapy or gender-affirming surgery, to align their body with their gender identity.\n\nAccessing medical help: There is no age limit on receiving medical help for transitioning. Healthcare professionals can offer psychotherapy, hormonal treatments, and surgical procedures to adults who want to transition.\n\nConsiderations for older individuals: Age-related factors may influence the recommendations from healthcare professionals. For instance, individuals over 50 may have a higher chance of developing certain health conditions, and their treatment plans may need to be adjusted accordingly.\n\nIt's important to consult with a doctor who understands transgender healthcare and to discuss the available options, potential risks, costs, and any specific concerns before making decisions regarding transitioning. \n (Source: Medical News Today, Medically reviewed by Francis Kuehnle)"),
    ("Sex after Surgery", "According to Johns Hopkins Medicine, people can have receptive intercourse or take part in any sexual activity 12 weeks after a vaginoplasty. Sexual activity before this may lead to delayed wound healing and complications. \n (Source: Medical News Today, Medically reviewed by Francis Kuehnle)"),
    ("Achieve Orgasm", "Following surgery, it can take time for people to recover and start to experience orgasms. When people undergo a vulvoplasty, the surgeon forms a clitoris from the head of the penis. This means most people will still be able to experience orgasms through clitoral stimulation. \n (Source: Medical News Today, Medically reviewed by Francis Kuehnle)"),
    ("Desire to have sex", "Transgender women may experience a decrease in sex drive after gender-affirming surgery. According to a 2020 article, people can stop taking anti-testosterone medication and may experience a decreased sex drive following an orchidectomy. Hormone replacement therapy may help maintain a regular sex drive. \n (Source: Medical News Today, Medically reviewed by Francis Kuehnle)"),
    ("vaginal depth after vaginoplasty", "An average vaginal depth after a vaginoplasty is 4–6 inches. For comparison, the average depth of a cisgender female’s vagina measures from 3.5 to 5 inches. In people who have a rectosigmoid vaginoplasty or colovaginoplasty, the vagina may have more depth. \n (Source: Medical News Today, Medically reviewed by Francis Kuehnle)"),
    ("Aftercare for vaginoplasty", "After a vaginoplasty, people need to use a vaginal dilator to stretch the vaginal canal and keep it open. Following surgery, people may need to dilate twice each day for a minimum of 15 minutes. This helps prevent loss of vaginal depth and width. A healthcare professional will provide instructions on how to safely and correctly use a dilator. Although people may experience some discomfort when they begin dilating, they should not experience any severe pain. \n (Source: Medical News Today, Medically reviewed by Francis Kuehnle)"),
    ("STI Protection after surgery", "According to the Terrence Higgins Trust, surgery can increase the risk of contracting STIs, as any unhealed skin can allow infections to pass more easily into the body. If people have had a vaginoplasty that uses part of the colon, a mucus membrane will line the vagina, making it easier for STIs to pass through. If people have had a vaginoplasty that uses penile and scrotal skin, the vagina is less susceptible to STIs, but any unhealed skin can still be a risk factor. Dilation of the vagina can also cause bleeding, so it is important to use a condom for any sex following dilation. \n (Source: Medical News Today, Medically reviewed by Francis Kuehnle)"),
    ("Hygiene tips after vaginoplasty", "After a vaginoplasty, it is important to keep the genital area clean and free of infection. People will need to keep the outside of the vagina dry. It may be useful to place an absorbent pad between the labia to soak up any excess moisture. Once the genital area is allowed to get wet, people should use soap and water to gently wash the area. It is important to avoid scrubbing or allowing shower spray to reach the surgical site. Johns Hopkins Medicine states that people will need to douche using a non-fragranced vaginal douche, beginning 8 days after surgery. Depending on how much vaginal discharge people have, douching may be required 1–2 times each week. More frequent douching may be necessary if there is a large amount of discharge. \n (Source: Medical News Today, Medically reviewed by Francis Kuehnle)"),
    ("Vaginoplasty procedure", "Vaginoplasty is typically a one-stage procedure. Some patients have their testicles removed (orchiectomy) before vaginoplasty, but this is not required. In fact, having the orchiectomy before your vaginoplasty can increase the risk of needing skin grafts. \n (Source: Johns Hopkins Medicine)"),
    ("Time during Vaginoplasty",
     "Most surgeries last between seven and 10 hours. \n (Source: Johns Hopkins Medicine)"),
    ("PrEP", "PrEP for Trans Women\n\nTransgender woman\n\u2022 PrEP, or pre-exposure prophylaxis, is a medication that helps you stay HIV-negative. When taken as prescribed, PrEP is highly effective. PrEP is safe and generally well tolerated. Most insurance plans (public and private) cover PrEP.\n\u2022PrEP works for women, men, people of transgender experience, people of all sexual orientations and gender identities, youth, and people who inject drugs.\n\u2022You can use PrEP alone or in combination with other prevention tools like condoms, PEP, and reduce your chances of getting HIV after sex. \n (Source: pleaseprepme.org)"),
    ("Hormones with PrEP", "It is safe to take hormones while using PrEP or PEP. Many people use Truvada as PrEP, as PEP, or as treatment for HIV, and Truvada does not reduce hormone levels. Although it's not expected that Descovy PrEP would reduce hormone levels, more research needs to be done to know for sure. Apretude PrEP (by injection) does not alter hormone levels. Both Truvada PrEP and Descovy PrEP should be used daily until more data are known \n (Source: pleaseprepme.org)"),
    ("Getting PrEP", "PrEP may be an option for you if:\n\n\u2022 You wonder how HIV impacts your life\n\u2022 Condoms are not used with partners of unknown HIV status\n\u2022 You or your partner(s) recently had gonorrhea or syphilis\n\u2022 You want to have sex without condoms with a partner who has HIV\n\u2022 You have sex for money, food, housing, and/or drugs\n\u2022 You inject drugs and share needles\n \n (Source: pleaseprepme.org)"),
    ("Vaginoplasty", "Vaginoplasty is surgery to create a vagina.\nIt involves removing the penis, testicles, and scrotum.\nVaginoplasty involves rearranging tissue in the genital area to create a vaginal canal (or opening) and vulva (external genitalia), including the labia.\n The surgeon uses a combination of the skin surrounding the existing penis along with the scrotal skin to create the vaginal canal.\nIf there is not enough skin available in the genital area, the surgeon may need to use a skin graft from the abdomen or thigh to construct a full vaginal canal.\n (Source: Johns Hopkins Medicine)"),
    ("Sexual Health Tests",
        """All sexually active gay and bisexual men should be tested regularly for STDs. The only way to know your STD status is to get tested (you can search for a testing site). Having an STD (like gonorrhea) makes it easier to get HIV or give it to others, so it’s important that you get tested to protect your health and the health of your partner. CDC recommends sexually active gay, bisexual, and other men who have sex with men test for: \n \u2022 HIV (at least once a year)
\u2022 Syphilis
\u2022 Hepatitis B
\u2022 Hepatitis C if you were born between 1945 to 1965 or with risk behaviors (see “how is hepatitis C spread”)
\u2022 Chlamydia and gonorrhea of the rectum if you’ve had receptive anal sex or been a “bottom” in the past year
\u2022 Chlamydia and gonorrhea of the penis (urethra) if you have had insertive anal sex (been on the “top”) or received oral sex in the past year
\u2022 Gonorrhea of the throat if you’ve given oral sex (your mouth on your partner’s penis, vagina, or anus) in the past year \n Sometimes your doctor or health care provider may suggest a herpes blood test. If you have more than one partner or have had casual sex with people you don’t know, you should be screened more often for STDs and may benefit from getting tested for HIV more often (for example, every 3 to 6 months). Your doctor can offer you the best care if you discuss your sexual history openly. Talk with your doctor about getting vaccinations for Hepatitis A and B, and HPV. \n 
(Source: Centers for Disease Control and Prevention, https://www.cdc.gov/msmhealth/for-your-health.htm)"""),
    ("Prevent Sexually Transmitted Diseases",
        "Vaccination:\n- Vaccines are safe, effective, and recommended ways to prevent hepatitis B and HPV. HPV vaccination is recommended for preteens ages 11 or 12 (or can start at age 9) and everyone through age 26, if not vaccinated already. Vaccination is not recommended for everyone older than age 26 years. However, some adults age 27 through 45 years who are not already vaccinated may decide to get the HPV vaccine after speaking with their doctor about their risk for new HPV infections and the possible benefits of vaccination. HPV vaccination in this age range provides less benefit as more people have already been exposed to HPV. You should also get vaccinated for hepatitis B if you were not vaccinated when you were younger.\n\nReduce Number of Sex Partners:\n- Reducing your number of sex partners can decrease your risk for STDs. It is still important that you and your partner get tested, and that you share your test results with one another.\n\n\
Use Condoms:\n- Correct and consistent use of the male latex condom is highly effective in reducing STD transmission. Use a condom every time you have anal, vaginal, or oral sex. If you have latex allergies, synthetic non-latex condoms can be used. But it is important to note that these condoms have higher breakage rates than latex condoms. Natural membrane condoms are not recommended for STD prevention. \n\n (Source: Centers for Disease Control and Prevention, https://www.cdc.gov/msmhealth/for-your-health.htm)"),
    ("HIV Test for Bisexual men", "If you’re a sexually active gay or bisexual man, you may benefit from more frequent testing (every 3 to 6 months). Talk to your health care provider about your risk factors and what testing options are available to you.  \n (Source: Centers for Disease Control and Prevention,https://www.cdc.gov/msmhealth/hiv.htm)"),
    ("Heath Issures in Bisexual men", "Research has shown that the following are some of the most common health concerns faced by gay and bisexual men. While they may not all apply to each individual, they are important concerns for men and their health care providers to be aware of.:\n\n- Intimate Partner Violence: Gay and bisexual men can experience intimate partner violence, which includes physical and emotional harm from a significant other. Seeking help is crucial, as it may involve manipulation and control, including threats to disclose their sexual orientation.\n\n- Substance Use Disorder: Gay and bisexual men have higher rates of tobacco and alcohol use due to stress and discrimination. This puts them at a greater risk for various health issues, including cancer and liver damage. Certain drugs, such as crystal meth, are also prevalent and contribute to unsafe sex and HIV transmission.\n\n- Body Dysmorphia: Gay and bisexual men have higher rates of body dysmorphia and eating disorders, influenced by factors like low self-esteem, discrimination, depression, and unrealistic body standards.\n\n- Reproduction and Fertility: Options such as surrogacy exist for gay and bisexual men in same-sex relationships who want to have children. It's important to find a provider or center that understands their specific needs and offers compassionate services.\n\n- Sexually Transmitted Infections: Men who have sex with men are at a higher risk for certain STIs. Using condoms consistently is the best method for prevention. Specific STIs of concern include HIV, syphilis, gonorrhea, hepatitis A and B, HPV, and meningitis.\n\n- Vaccinations: Vaccines are available to prevent hepatitis A and B, and men who have sex with men can receive a vaccine against certain forms of HPV.\n\nIt's crucial for gay and bisexual men to prioritize their health, seek appropriate healthcare providers, and access resources tailored to their needs. \n (Source: Johns Hopkins Medicine)"),
    ("Heath Issures in Lesbian and Bisexual ", "Research has shown that the following are some of the most common health concerns faced by lesbian and bisexual women. While they may not all apply to everyone, they are important concerns for lesbian and bisexual women and their health care providers to be aware of.\n\n- Breast Exams\n- Intimate Partner Violence\n- Substance Use Disorder\n- Obesity\n\n- Sexual Health:\n\t -- Pap Tests\n\t -- Contraception\n\t --Pregnancy and Fertility\n- HPV \n (Source: Johns Hopkins Medicine)"),
    ("Pap Test", "A Pap test, along with a pelvic exam, is an important part of your routine healthcare. It can help find abnormal cells that can lead to cancer. Your healthcare provider can find most cancers of the cervix early if you have regular Pap tests and pelvic exams. Cancer of the cervix is more likely to be successfully treated if it is found early.\n The Pap test is useful for finding cancerous cells, and other cervical and vaginal problems such as precancerous cells and inflammation. \n (Source: Johns Hopkins Medicine)"),
    ("Protection from STD ", "The best way to prevent getting an STD is to not have any type of sexual activity, including oral, vaginal, and anal sex. But you can take several steps to lower your risk for an STD if you decide to become sexually active, or are currently sexually active. These include:\n\n- Any sexual relationship should be with only one uninfected partner. That partner should also not have any other partners.\n- Use a latex condom the correct way every time you have sex. Or use a female polyurethane condom plus medicine that kills sperm (topical microbicide).\n- Use sterile needles if you inject IV medicines.\n- Prevent and control other STDs. This will lower your risk for human papillomavirus (HPV).\n- Delay having sexual relationships as long as you can. The younger you are when you start having sex, the more likely you are to get an STD.\n- Have regular checkups for HIV and STDs.\n- Learn the symptoms of STDs and seek medical help as soon as possible if any symptoms develop.\n- Don't have sexual intercourse during your monthly period.\n- Don't have anal intercourse. Or use a latex condom and medicine that kills sperm.\n- Don't douche.\n- Some people may get help in preventing HIV infection by taking a special medicine (pre-exposure prophylaxis). Talk with your healthcare provider to see if it is right for you. \n (Source: Johns Hopkins Medicine)"),
    ("Most Common STD", "The common STDs are:\n- HIV\n- Human papillomavirus (HPV)\n- Chlamydia\n- Gonorrhea\n- Genital herpes\n- Syphilis \n (Source: Johns Hopkins Medicine)"),
    ("STD", "STDs are infectious diseases passed from person to person through sexual contact. Millions of new cases happen every year in the U.S. Half of the new infections happen in people between the ages of 15 and 24 years. \n (Source: Johns Hopkins Medicine)"),
    ("HIV", "HIV is a virus that destroys the body's ability to fight off infection. People who have HIV may not look or feel sick for a long time after infection. But if you are not diagnosed early and treated, you will eventually become very likely to get many life-threatening diseases and certain forms of cancer.\n- The virus is passed on most often during sexual activity. It can also be passed on by sharing needles used to inject IV drugs.\n- HIV can be passed to your baby during pregnancy, labor, delivery, and through breastfeeding. If you know early in your pregnancy that you are HIV positive, you can get treatment that greatly lowers your chance of passing on the virus to your child, the CDC says. \n (Source: Johns Hopkins Medicine)"),
    ("Sexual Health Tests",
        """All sexually active gay and bisexual men should be tested regularly for STDs. The only way to know your STD status is to get tested (you can search for a testing site). Having an STD (like gonorrhea) makes it easier to get HIV or give it to others, so it’s important that you get tested to protect your health and the health of your partner. CDC recommends sexually active gay, bisexual, and other men who have sex with men test for: \n \u2022 HIV (at least once a year)
\u2022 Syphilis
\u2022 Hepatitis B
\u2022 Hepatitis C if you were born between 1945 to 1965 or with risk behaviors (see “how is hepatitis C spread”)
\u2022 Chlamydia and gonorrhea of the rectum if you’ve had receptive anal sex or been a “bottom” in the past year
\u2022 Chlamydia and gonorrhea of the penis (urethra) if you have had insertive anal sex (been on the “top”) or received oral sex in the past year
\u2022 Gonorrhea of the throat if you’ve given oral sex (your mouth on your partner’s penis, vagina, or anus) in the past year \n Sometimes your doctor or health care provider may suggest a herpes blood test. If you have more than one partner or have had casual sex with people you don’t know, you should be screened more often for STDs and may benefit from getting tested for HIV more often (for example, every 3 to 6 months). Your doctor can offer you the best care if you discuss your sexual history openly. Talk with your doctor about getting vaccinations for Hepatitis A and B, and HPV. \n 
(Source: Centers for Disease Control and Prevention, https://www.cdc.gov/msmhealth/for-your-health.htm)"""),

    ("Sexual Health Tests in Bisexual men", """All sexually active gay and bisexual men should be tested regularly for STDs. The only way to know your STD status is to get tested (you can search for a testing site). Having an STD (like gonorrhea) makes it easier to get HIV or give it to others, so it’s important that you get tested to protect your health and the health of your partner. CDC recommends sexually active gay, bisexual, and other men who have sex with men test for: \n \u2022 HIV (at least once a year)
\u2022 Syphilis
\u2022 Hepatitis B
\u2022 Hepatitis C if you were born between 1945 to 1965 or with risk behaviors (see “how is hepatitis C spread”)
\u2022 Chlamydia and gonorrhea of the rectum if you’ve had receptive anal sex or been a “bottom” in the past year
\u2022 Chlamydia and gonorrhea of the penis (urethra) if you have had insertive anal sex (been on the “top”) or received oral sex in the past year
\u2022 Gonorrhea of the throat if you’ve given oral sex (your mouth on your partner’s penis, vagina, or anus) in the past year \n Sometimes your doctor or health care provider may suggest a herpes blood test. If you have more than one partner or have had casual sex with people you don’t know, you should be screened more often for STDs and may benefit from getting tested for HIV more often (for example, every 3 to 6 months). Your doctor can offer you the best care if you discuss your sexual history openly. Talk with your doctor about getting vaccinations for Hepatitis A and B, and HPV. \n 
(Source: Centers for Disease Control and Prevention, https://www.cdc.gov/msmhealth/for-your-health.htm)"""),
("Resources for LGBTQ+ Youth", """- Because some LGBTQ+ Youth are more likely than their heterosexual peers to experience bullying or other aggression in school, it is important that educators, counselors, and school administrators have access to resources and support to create a safe, healthy learning environment for all students.\n - Advocates for Youth (AFY): LGBTQ Resources for Professionals\n \t- Lesson plans, tips and strategies, background information, and additional resources to help youth-serving professionals create safe spaces for young people of all sexual orientations and gender identities.\n
- American Psychological Association (APA) Resources:\n \t- Just the Facts: A Primer for Principals, Educators, and School Personnel\n \t\t- Just the Facts provides information and resources for principals, educators, and school personnel who confront sensitive issues involving gay, lesbian, and bisexual students.\n \t- Safe and Supportive Schools Project\n \t\t- The Safe and Supportive Schools Project promotes safe and supportive environments to prevent HIV and other sexually transmitted infections among adolescents.\n - Creating Safer Spaces in Schools for LGBTQ Youth | The Trevor Project\n \t- The Trevor Project is a national organization providing crisis intervention and suicide prevention services to lesbian, gay, bisexual, transgender, and questioning (LGBTQ) young people under 25.\n - Educator Resources | GLSEN\n \t- GLSEN educator guides and lessons to support your curriculum and practices.\n - Genders & Sexualities Alliance Network\n \t- GSA clubs are student-run organizations that unite LGBTQ+ and allied youth to build community and organize around issues impacting them in their schools and communities.\n - Q Chat Space\n \t- Q Chat Space is a digital LGBTQ+ center where teens join live-chat, professionally facilitated, online support groups. Also available in Spanish (disponible en español).\n - StopBullying.gov: Information for LGBTQ Youth\n \t- Lesbian, gay, bisexual, transgender, or questioning (LGBTQ) youth and those perceived as LGBT are at an increased risk of being bullied. There are important and unique considerations for strategies to prevent and address bullying of LGBTQ youth.\n - Supporting LGBTQ+ Students – Micro-credentials | National Education Foundation\n \t- This stack of six micro-credentials is designed to help educators understand how to create a safe and inclusive classroom environment for LGBTQ+ students.\n - The Trevor Project: Education and Resources for Adults\n \t- The Trevor Project’s “Trainings for Professionals” include in-person Ally and CARE trainings designed for adults who work with youth. These trainings help counselors, educators, administrators, school nurses, and social workers discuss LGBTQ-competent suicide prevention.""

 \n (Source: Centers for Disease Control and Prevention, https://www.cdc.gov/lgbthealth/youth-resources.htm)""),"
("Reseources for LGBT health", "- General Information\n- Healthy People 2030\n- Advancing Effective Communication, Cultural Competence, and Patient- and Family-Centered Care for the Lesbian, Gay, Bisexual, and Transgender (LGBT) Community, A Field Guide (The Joint Commission)\n- Health of Lesbian, Gay, Bisexual, and Transgender People: Building a Foundation for Better Understanding (The Institute of Medicine)\n- Data Resources\n- LGBTData.com (Drexel University)\n- Data Resources from the Center for Population Research in LGBT Health (ICPSR)\n- LGBT Health-Related National Organizations/Coalitions\n- Fenway Institute\n- GLMA: Health Professionals Advancing LGBT Equality\n- LGBT HealthLink Network\n- National Association of Lesbian and Gay Addiction Professionals\n- National LGBT Cancer Network\n- OutCare Health \n (Source: Centers for Disease Control and Prevention, https://www.cdc.gov/lgbthealth/links.htm)"""),



]
