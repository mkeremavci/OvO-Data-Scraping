# OvO-Data-Scraping

### Collected Data Links

["14 Mayıs 2023 Cumhurbaşkanlığı Seçimi Oy ve Ötesi Açıklanan Sonuçlar"](https://drive.google.com/file/d/1ucE5IQZeiLNdK-ROgOpF91bXGTfQkljV/view?usp=sharing)

["14 Mayıs 2023 Cumhurbaşkanlığı Seçimi Oy ve Ötesi Tutanak Linkleri"](https://drive.google.com/file/d/1G2lPwNvOp3zi9CdQKA-W8pi0XioGVFBn/view?usp=sharing)

["14 Mayıs 2023 Milletvekili Genel Seçimi Oy ve Ötesi Açıklanan Sonuçlar"](https://drive.google.com/file/d/1cQTRffSD-1hYPj--KoU5ggYRxPh67l-2/view?usp=sharing)

["14 Mayıs 2023 Milletvekili Genel Seçimi Oy ve Ötesi Tutanak Linkleri"](https://drive.google.com/file/d/1q6N6MHOXfHTEGNDpGjTU3CF_TV3v7KPF/view?usp=sharing)

[Raw Data](https://drive.google.com/file/d/1iHhHIgjPOupt70HXYi_t0Iq0P3Yu6rue/view?usp=sharing)

[Raw Data v2](https://drive.google.com/file/d/1RySPU-_qsEkyEeidifEnzHOmW_HNfdDt/view?usp=sharing)

### Metadata

We first gathered school ids to scrape the results of each polling center easily via the OvO API. You can use the command below to collect this metadata:

    python collect_meta.py

### Collecting Election Results

You should use the command below to collect the election results of each poll with the Ovo API:

    python main.py

### Processing Data

You should use the following command to post-process the data:

    python process.py

    
