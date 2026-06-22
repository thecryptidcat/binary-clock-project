# First project - creating a functional binary clock

As of creating this repo, I've already made a functional version that's relatively optimised. Now it's working with the initial features I wanted, I'll be updating it here as I improve and add other things to it.

### Required Python packages:

I will eventually create the required packages through GitHub's method of doing so. Currently have no idea how it works, so will get to that, for now just make sure you have these installed when you run the code.

- customtkinter

---

### Initial features:

- Accurate representation of the time
- Start and stop buttons
- Time split into each column (HH:MM:SS) and each shown vertically to be their binary representation
- Each '1' changes the display green to create the clock display

### Added since 1.0:

- Making columns only display their required amount of bits

### Future features/amendments:

- Polishing the UI and making the display a bit easier to read
- Adding customisability, including:
- - general window customising e.g bg colour, fonts
- - the option whether to show the 1 or 0 digits on the buttons
- - changing the colour of the on (and might as well off too) modes of each button
- General optimising of the code

## Known bugs

- [x] ~~About 1 in every 20 seconds is skipped on the text timer and so the clock display. It still displays correctly, but updates slightly out of sync to the real time.~~</p>
Sometimes the program runs fine, sometimes it likes to be slightly buggy and skip a second on the display, on the timer, or both. Fixed the recurring issue but will look into this new one further.

---

### About

The origin of the idea for this project came from when I was messing around with (a version of) Scratch. I used to mess with Scratch a lot when I was younger, and so when I was reintroduced to a version of it again years later I wanted to experiment a bit with it. Hence, the idea for a binary clock showed up. No idea where from other than I came up with it and it sounded cool, and like a challenge that I knew roughly how I'd execute.

I didn't quite finish it back then, but I got the basic foundation of it working. Since starting Python back up again, it seemed like a good starting point considering I had something somewhat direct to follow. It certainly was a bit more difficult and painful to figure out than I thought it'd be, but that's just an indicator of learning, so it was worth it. Version 1.0 is likely absolutely terrible to look at by someone who's even remotely versed in Python, however it was a big starting point for me and I got there, so I'm quite proud of it.
