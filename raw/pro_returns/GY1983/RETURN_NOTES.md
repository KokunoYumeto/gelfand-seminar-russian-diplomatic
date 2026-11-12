# GY1983 (records 597 and 599-639, 1983-85): how this return was received, 12 Nov 2026

Produced by GPT-6 Astra (ChatGPT Pro mode). Three Gelfand prompts ran at the same time overnight, and the
execution environment of this run failed. Pro therefore delivered its ZIP as base64 in the chat ("GY1983 complete
source archive recovery"). Claude decoded it with its own script, not Pro's restore script:
- SHA-256 1718e0c9e91870feb064151976e39feeff1b5332ff37ab82b29480b17eff5bfc, matching the digest Pro printed;
- the zip test passed;
- 49 members, extracted here.

The copy saved in the user's ChatGPT space is byte-identical.

- **No compiled PDF:** XeLaTeX lacked its format files in Pro's environment.
- **The chapter needs rebuilding:** the supplied builder was lost there, so `GY1983_chapter.tex` was rendered by
  Pro's recovery renderer `GY1983_render.js`. Rebuild the chapter with the kit's `build_chapter.py`.
- **The partial text recovery adds nothing:** it covers records 631-639 (78 items). Of these, 77 are identical to
  the archive, and in the one other item the formula lost its backslashes.

Pro's code is published, not run.
