**28th Dec 2024**
Further changes to this fork. (Version 0.06)

Reorganized this skins contents so that it can be managed by weectl extension.
There are still some manual steps required, but it should be more managable and straightforward now.
Any problems with these changes - raise an issue above.

The original, built in timing method of "refresh_interval" did not work and has now been removed. To control the generation interval for this skin then [an appropriate stanza](https://www.weewx.com/docs/5.0/custom/report-scheduling/) is preset in the [[AllTimeSeasons]] section of weewx.conf.

The default is set at 10 minutes, you can of course change it.

<pre>
  [[AllTimeSeasons]
  [...]
  report_timing = '*/10 * * * *'  # default timing
</pre>

Change summary.
  *Integrate files into a weewx style installable skin.
  *Remove refresh_interval code and replace it with the timing_report method.
  *historygenerator.py has been reworked to use the Weewx v4 style logging.
  *Catch a TypeError exception in the summary column, due to missing ('-') entries in the monthly values..


To install this skin addition...

   # Download

    wget -O weewx-AllTimeSeasons.zip https://github.com/glennmckechnie/alltimeSeasons/archive/refs/heads/master.zip

   # Run the installer:

   For weewx 5.x...

     weectl extension install weewx-AllTimeSeasons.zip

   or the older 4,x versions use...

     wee_extension --install weewx-AllTimeSeasons.zip

  # Modify skins/Seasons/index.html.tmpl

  Before you make changes any changes to index.html.tmpl, make a backup of it.
    
  To add the menu item to the Seasons skin, 2 new lines need to be included within the **skins/Seasons/index.html.tmpl** file
  
  So these lines...
  
            <a class="button" id="button_history_alltime"
               onclick="choose_history('alltime')">All-time</a>
  
   Will be inserted into the history_widget section, as follows...
   
  N.B. ([...] substitutes for repetitive content. Content that has been removed for clarity. Ignore it.)
  
      <div id="plot_group">
        <div id="history_widget" class="widget">
          <div id="plot_title" class="widget_title">History:&nbsp;&nbsp;
            [...]
            <a class="button" id="button_history_alltime"
               onclick="choose_history('alltime')">All-time</a>
          </div>
          <div id="history_day" class="plot_container">


  This skin now generates historygenerator.inc and places it in your default WWW_ROOT folder. The Seasons skin needs to be able find and include this files content when its index.htm.tmpl is generated. This is done by specifying the absolute path as in the example below. This example assumes that /var/www/html is your web server location ( your WWW_ROOT).
  
  The second addition to the **skins/Seasons/index.html.tmpl** file consists of the 3 lines starting with #.
  
          #if os.path.exists("/var/www/html/histgenerator.inc")
             #include "/var/www/html/histgenerator.inc"
          #end if
  
  These will be inserted above the footer section, as follows...
  
          <div id="history_year" class="plot_container" style="display:none">
          [...]
          </div>
          #if os.path.exists("/var/www/html/histgenerator.inc")
             #include "/var/www/html/histgenerator.inc"
          #end if
          </div>
  
  # Optional:
  Ideally, the historygenerator.inc file will exist when your main skin (Seasons) StdReport section runs. That requires the [[AllTimesSeasons]] section in weewx.conf to run first.  To do that, then move the [[AllTimeSeasons]] section to before the Seasons skin section in the weewx.conf file.
  It will work without that change, the only difference is it won't be picked up until the next report cycle ie:- it will be slightly older - which hardly matters as the default is to generate it every 10 minutes.

  # Uninstall

   Use weewctl extension to uninstall the extension, then **restore your original index.html.tmpl** (that you backed up).

   For weewx 5.x...

    weectl extension uninstall weewx-AllTimeSeasons.zip

   or the older 4,x versions use...

    wee_extension --uninstall weewx-AllTimeSeasons.zip

 Notes regarding older changes have been moved to the bottom of this page.
 Gedgers original description and notes are immediately below

=========== End of fork changes =========

=========== Original Description =========


# alltimeSeasons skin

## Summary
These files modify the included weewx skin Seasons to include all-time data. 

## Overview
I wanted to be able to compare the rainfall in May with rainfall last year, well in fact all the years my weather station has been operating. 
I also wanted to able to compare temperature and perhaps wind. Surprisingly the standard weewx installation doesnt include this facility but 
due to its excellent design it's fairly straightforward to add a new skin to do what you want. I really liked the, now standard, Season skin so I used 
that as a starting point. Here are some screen shots of the results.

<img src="screenshots/Frontpage.png" alt="Frontpage" width="200"/>&nbsp;&nbsp;&nbsp;&nbsp;<img src="screenshots/Statistics.png" alt="Statistics" width="200"/>

## Solution

The grunt of the work was done by brewster76 with his new skin using Bootstrap, indeed you may prefer his solution as it also includes gauges 
and a full installer. Check it out here https://github.com/brewster76/fuzzy-archer

I used his, very slightly modified, python code to generate the actual historic tables and then modified the Seasons template to include the results.

## Installation

This is a manual install.

First make a copy of the Seasons skin including all the sub directories. I called mine alltimeSeasons.

Then replace the files in the new alltimeSeasons with those provided here.

Then copy the historygenerator.py file provided in the user/bin directory to the user bin directory in your weewx installation. Note this is different depending on how you installed weewx. If you installed via DEB/RPM then its /usr/share/weewx/user if you installed using setup.py then its /home/weewx/bin/user.

Finally edit your weewx.conf file and change the skin to your new skin, I just changed the original to point to the new location.

        [[SeasonsReport]]
                # The SeasonsReport uses the 'Seasons' skin, which contains the
                # images, templates and plots for the report.
                skin = alltimeSeasons
                enable = true

In theory that's all. However, although I have done this on my own system I haven't actually followed these instructions on a clean install to confirm they work. If you try you may well be the first. If you find a problem then please let me know and I'll do my best to correct it.

NOTE: This has only been tested with weewx V4.00 and later

==== History of Fork changes ===

*30 Oct 2022*

The alltimeSeasons addition takes the NOAA data (Monthly/ Yearly Reports) and presents some of the Temperature and Rainfall stats as colored html.

Changes to the original repo at https://github.com/gedger/alltimeSeasons that this was forked from are...

Reorganized repo files.

Moved the original files to weewx410 (the version that the files appear to have come from)

Added weewx460 and weewx491 directories with their respective files. Those files can replace your existing Season skin files, or if you've already modified then use the diffs.
The 'diffs' are .html files that show what has changed for each version. Use either html diff (or both) to assist with the changes. They are included in the hope they clarify what needs to be done.

The historygenerator.py file belongs in the weewx directory -- bin/user/historygenerator.py

After installation, restart weewx for changes to take affect.

Bugfix:

Modified historygenerator.py to break on success (resolves duplicate style strings)

Enhancement:

Added weewx4 style logging to historygenerator.py

Style changes:

Modified layout to show "out of bounds" values as red text.

Change 'Total' columns to white backgrounds with bold text.

Output html passes https://validator.w3.org tests.

