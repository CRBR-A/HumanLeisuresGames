# ChroniclesRPG System - Community Edition

Welcome to our GitLab! ChroniclesRPG was originally developed by BossGames as a Public Domain Tabletop RPG System. While BossGames maintains their own version, this version was started from BossGames edition of ChroniclesRPG-V.2 and is meant to be developed by public interests. For that reason, this GitLab is open to the public and the links for it are on the ChroniclesRPG.com website (which is probably where you just came from). Please feel free to read over the system and if you think you can improve it, please create a fork of it (I think I'm using that word correctly, I'm new to running this Git stuff) and produce your changes and send in a merge request. The Maintainers will include your work if possible and only only exclude content if it conflicts with existing contributions. ChroniclesRPG was built with Mods in mind, so for the most part if you have an idea for something that should be included in ChroniclesRPG then write a Mod at first. This ensures maximum compatibility with other content contributors. From there, it will be available to other creators and it will naturally work its way in to other works.

The files included in this GitLab project are, unless otherwise specified, licensed under Creative Commons 0 (So they are available as public domain material without restriction).

The download links below are for a PDF that is compiled automatically when each of these two branches are updated with a merge request. So whenever something is pushed to CI, it will generate a new PDF under the "Latest" link. Whenever something is pushed to Main, it will generate a new PDF under the "Stable" link. These links are also on the ChroniclesRPG website under "ChroniclesRPG - Community Edition".

You can find contact methods at the ChroniclesRPG.com website if you want to just make some suggestions. We have a Discord server for everyone to talk about the project and share information at. There is a "Development" section on that Discord server where contributors can communicate while working on the ChroniclesRPG System.

  
|            Stable              |
|:---------------------------------:|
| [Download PDF][stablepdf]|
| [Download EPUB][stableepub]|
| [Download HTML][stablehtml]|
  
  
|            Latest              |
|:---------------------------------:|
| [Download PDF][latestpdf]|
| [Download EPUB][latestepub]|
| [Download HTML][latesthtml]|

As well, if you would like to integrate this rules set into your own website, this is a link to an HTML conversion of the rules document:

https://chroniclesrpg.gitlab.io/chronicles-core/

This document will rebuild every time that changes are pushed to the Main branch of this project, so this link will stay up to date with the final changes.

Chronicles Core is an open-licensed tabletop RPG.

[stablepdf]: https://gitlab.com/chroniclesrpg/chronicles-core/-/jobs/artifacts/main/raw/Chronicles_Core.pdf?job=compile_pdf
[stableepub]: https://gitlab.com/chroniclesrpg/chronicles-core/-/jobs/artifacts/main/raw/Chronicles_Core.epub?job=compile_pdf
[stablehtml]: https://gitlab.com/chroniclesrpg/chronicles-core/-/jobs/artifacts/main/raw/Chronicles_Core.html?job=compile_pdf
[latestpdf]: https://gitlab.com/chroniclesrpg/chronicles-core/-/jobs/artifacts/ci/raw/Chronicles_Core.pdf?job=compile_pdf
[latestepub]: https://gitlab.com/chroniclesrpg/chronicles-core/-/jobs/artifacts/ci/raw/Chronicles_Core.epub?job=compile_pdf
[latesthtml]: https://gitlab.com/chroniclesrpg/chronicles-core/-/jobs/artifacts/ci/raw/Chronicles_Core.html?job=compile_pdf
  
# ChroniclesRPG System - A Summary
The ChroniclesRPG System is an entirely D6 based system. It revolves around the use of **"Dice Groups"** which are up to four D6, and around the use of Epxerience Points which are used to add dice to Dice Groups. Dice Groups are used to make checks with. There are different types of Dice Groups, each with their own scope of uses and unique properties.

**"Talents"** are Dice Groups that have a minimum of one die in them by default. The ten Talents represent the character's default capabilities and limitations. Whenever a character is Harmed, their Talents are impacted, which temporarily reduces the number of dice in the affected Talents. This normally occurrs through an Injury resulting from an Attack or other harmful circumstance. The Vitality Talent represents a characters ability to maintain their life in the face of harmful effects. If a character's Vitality Talent is Injured whenever the character has only one die in it, then that character must roll one D6. If the result is a 4-6, then they drop unconscious but live, otherwise they die.

There are a set of **"Mod Packages"** toward the end of the ChroniclesRPG System document. These are excluded from gameplay by default, so that the GM or Game Designer can bring that content into the game when it is most fitting. This ensures that core gameplay is not disturbed when including that content would otherwise disturb it.

One of these Mod Packages is the **"Engineering System"**. This Mod introduces a Dice Group called "Creation Dice", Functions which represent core accomplishments of a Creation, and then Minor, Major and Epic Creations. Creations are things that a character has made from their resources, knowledge and skill. These things are external to the character and provide certain defined benefits to whoever may be using them. A character can enhance their understanding of how to engineer Creations by learning Functions, which describe certain things that a Creation can do. They then use their Creation Dice to determine how long preparing the Creation will take (which results in Dice Groups added to the Creation), then they assign Functions to the Dice Groups of that Creation. The Creation then uses those Dice Groups to make checks whenever it uses its Functions to do somthing and if it takes damage then it loses one or more dice in its Dice Groups.  

Another Mod is the **"Abilities"** Mod. This Mod introduces Dice Groups called "Power Dice" and Abilities, which can be organized by the GM or Game Designer into any sort of Ability/Feature system to provide unique character creation options for the players IE: Arcane Magic, Mutant Powers, Divine Actions etc...
The systems presented in this Mod are supposed to be able to be stretched to fit any need that requires unique, specific effects-as-character-options.
To summaraize it, you acquire Power Dice by spending Experinence Points (One per die by default). Then you acquire Abilities (One per die by default) and assign each Ability to a group of Power Dice. Each Ability has a Value (1-4) and a Type (Minor, Major or Epic). An Ability can only be assigned to a Power Dice Group that has a number of dice in it equal to or less than the Ability's Value. Minor Abilities do not drain their Power Dice, Major Abilities risk draining their Power Dice and Epic Abilities always drain their Power Dice. Also, whenever an Ability is used to make a check, that check is made using its Power Dice.

There's much more detail that makes the system work like it does, but these are the high-level points that can give a big picture view of the system.
