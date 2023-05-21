# OvO-Data-Scraping

## Contact Info

[Twitter](https://twitter.com/keremdotpy), [Mail](mkeremavci@gmail.com)

## Data

["14 Mayıs 2023 Cumhurbaşkanlığı Seçimi Oy ve Ötesi Açıklanan Sonuçlar"](https://drive.google.com/file/d/1ucE5IQZeiLNdK-ROgOpF91bXGTfQkljV/view?usp=sharing)

["14 Mayıs 2023 Cumhurbaşkanlığı Seçimi Oy ve Ötesi Açıklanan Sonuçlar" v2](https://drive.google.com/file/d/1cTWkn6fW6-HL9DRvcxYJ0HIE7N1ww6km/view?usp=sharing)

["14 Mayıs 2023 Cumhurbaşkanlığı Seçimi Oy ve Ötesi Tutanak Linkleri"](https://drive.google.com/file/d/1G2lPwNvOp3zi9CdQKA-W8pi0XioGVFBn/view?usp=sharing)

["14 Mayıs 2023 Cumhurbaşkanlığı Seçimi Oy ve Ötesi Tutanak Linkleri" v2](https://drive.google.com/file/d/1RIGRMneQvMtD6u8xOHjBLgIDTiIMCMNT/view?usp=sharing)

["14 Mayıs 2023 Milletvekili Genel Seçimi Oy ve Ötesi Açıklanan Sonuçlar"](https://drive.google.com/file/d/1HQhZ5zeckyveKCsOuS5CV9P9JOdYXwT_/view?usp=sharing)

["14 Mayıs 2023 Milletvekili Genel Seçimi Oy ve Ötesi Açıklanan Sonuçlar" v2](https://drive.google.com/file/d/1cQTRffSD-1hYPj--KoU5ggYRxPh67l-2/view?usp=sharing)

["14 Mayıs 2023 Milletvekili Genel Seçimi Oy ve Ötesi Tutanak Linkleri"](https://drive.google.com/file/d/1aRQU8DIshPtmNBMwyPz_JsozBBfwuO_v/view?usp=sharing)

["14 Mayıs 2023 Milletvekili Genel Seçimi Oy ve Ötesi Tutanak Linkleri" v2](https://drive.google.com/file/d/1q6N6MHOXfHTEGNDpGjTU3CF_TV3v7KPF/view?usp=sharing)

["14 Mayıs 2023 Seçimleri Sandık Listesi"](https://drive.google.com/file/d/15mLyFlV6-pX7Lej7QNEHsJqtIH8rzztu/view?usp=sharing)

["14 Mayıs 2023 Seçimleri YSK Sandık İstatistikleri"](https://docs.google.com/spreadsheets/d/1RchxSJlEYjN8dXi0nn5ROEaRApsXMQ5R/edit?usp=sharing&ouid=110274593961655206191&rtpof=true&sd=true)

[Raw Data](https://drive.google.com/file/d/1iHhHIgjPOupt70HXYi_t0Iq0P3Yu6rue/view?usp=sharing)

[Raw Data v2](https://drive.google.com/file/d/1RySPU-_qsEkyEeidifEnzHOmW_HNfdDt/view?usp=sharing)

[Raw Data v3](https://drive.google.com/file/d/1ycxpSFiaY9ccLybjTOk1nbRBitU_Qm6G/view?usp=sharing)

## Scripts

### Metadata

We first gathered school ids to scrape the results of each polling center easily via the OvO API. You can use the command below to collect this metadata:

    python collect_meta.py

### Collecting Election Results

You should use the command below to collect the election results of each poll with the Ovo API:

    python main.py

### Processing Data

You should use the following command to post-process the data:

    python process.py
