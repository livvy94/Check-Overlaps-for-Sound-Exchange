I work at a local radio station. At my job, one of my tasks is reporting which songs played over the air during two whole weeks for every quarter of the year.

The station mostly broadcasts NPR news shows like [Fresh Air](https://whyy.org/programs/fresh-air/) and [All Things Considered](https://www.npr.org/programs/all-things-considered/), but we have a handful of music programs on Saturdays and Sundays - specifically, locally-produced blues, folk, and jazz shows. Some of these shows are still completely run with physical CDs instead of via playlists on a computer.

I have to formulate and send in tab-separated variable (tsv) files with the following format:

| Title                    | Artist                       | Album                              | Label               | Start Time         | End Time           |
|--------------------------|------------------------------|------------------------------------|---------------------|--------------------|--------------------|
| Pickaway                 | Greg Cahill & Don Stiernberg | Blueskies                          | Turquoise           | 2/16/2025 18:06:00 | 2/16/2025 18:07:59 |
| Hello                    | David Grisman                | David Grisman Rounder Compact Disc | Rounder             | 2/16/2025 18:08:00 | 2/16/2025 18:08:17 |
| Callin' in the Dogs      | Tad Marks                    | Callin' in the Dogs                | Crop Circle         | 2/16/2025 18:09:00 | 2/16/2025 18:11:33 |
| Another Day              | Gene And Gayla Mills         | Walk On Solid Ground               | Heartpine music     | 2/16/2025 18:12:00 | 2/16/2025 18:14:59 |

(etc, etc...)

Usually, the hosts send me Excel spreadsheets with the wrong format, and I have to do a lot of work to get the data into this specific format (day/month/year, army time with seconds). AND, usually, the seconds are wrong and it gives you errors when you try to upload the `.tsv` file. So, I wrote this tool. It outputs the following:

```
Overlap detected between 'Heaven's Joy Awaits' and 'Lullaby' (12 sec)
Overlap detected between 'Wondrous Love, Lay Aside Your Crown' and 'Dear Mary' (42 sec)
Overlap detected between 'Wildflowers' and 'Long Time Friends' (36 sec)
Overlap detected between 'Oscar & Minnie' and 'Softly and Tenderly' (52 sec)
```
(etc, etc...)

This helps me tremendously. Hopefully somebody else finds this useful too. 
