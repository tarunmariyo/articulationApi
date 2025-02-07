from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Sample exercises for each phoneme
EXERCISES = {
    "b": {
        "description": "Make the 'B' sound by pressing your lips together and releasing air while voicing: 'buh'. Try saying 'ball' or 'bat'.",
        "videos": ["https://youtu.be/746Aq0ndZy0?si=EmuuYVEZbgZtbQ-i"]
    },
    "c": {
        "description": "For the 'C' or 'K' sound, raise the back of your tongue to touch the roof of your mouth, then release with a burst of air: 'kuh'. Try 'cat' or 'kite'.",
        "videos": ["https://youtu.be/0z80Zt66RcU?si=NetUjmYCsm41Td12"]
    },
    "d": {
        "description": "Place your tongue behind your upper front teeth and release quickly while voicing: 'duh'. Try saying 'dog' or 'door'.",
        "videos": ["https://youtu.be/61xe97Nf8J4?si=WjGvdsIr2i_enTNU"]
    },
    "f": {
        "description": "Gently place your top teeth on your lower lip and blow air out to make the 'F' sound: 'fff'. Try 'fish' or 'fun'.",
        "videos": ["https://youtu.be/xA61MYdspgM?si=s7FekF9psGSRn3a8"]
    },
    "g": {
        "description": "The 'G' sound is made by lifting the back of your tongue to touch the soft part of the roof of your mouth: 'guh'. Try 'goat' or 'game'.",
        "videos": ["https://youtu.be/bSlb9yscpbw?si=6xDZemT5YZ7dzMZw"]
    },
    "h": {
        "description": "For the 'H' sound, breathe out softly from your throat without using your voice: 'huh'. Try 'hat' or 'happy'.",
        "videos": ["https://youtu.be/3-qJF9ZstLQ?si=b3ougOIk6Gb91dSi"]
    },
    "j": {
        "description": "The 'J' sound is made by touching your tongue to the roof of your mouth and releasing with a voiced sound: 'juh'. Try 'jump' or 'juice'.",
        "videos": ["https://youtu.be/xETjN3Y24cQ?si=P_Ot9L-Yf9ixvYhR"]
    },
    "k": {
        "description": "Like the 'C' sound, make the 'K' by pressing the back of your tongue against the roof of your mouth: 'kuh'. Try 'kite' or 'kick'.",
        "videos": ["https://youtu.be/JwKKfHIpOX8?si=pXhlNBBs7eSgj6X4"]
    },
    "l": {
        "description": "To say 'L', lift the tip of your tongue to touch just behind your upper front teeth and let the air flow around it: 'lll'. Try 'lion' or 'light'.",
        "videos": ["https://youtu.be/_IAEg3igJVI?si=4XMyQmXSTzMWSHIU"]
    },
    "m": {
        "description": "Close your lips and hum through your nose to make the 'M' sound: 'mmm'. Try 'monkey' or 'moon'.",
        "videos": ["https://youtu.be/0VCeITL8P4E?si=wkwYbJP8642lrXVI"]
    },
    "n": {
        "description": "For 'N', place your tongue behind your top teeth and let air pass through your nose: 'nnn'. Try 'nose' or 'net'.",
        "videos": ["https://youtu.be/oun0cGPMHZQ?si=xTBBvMTDWhwDsmHo"]
    },
    "p": {
        "description": "Press your lips together, then release a small burst of air without using your voice: 'puh'. Try 'penguin' or 'pie'.",
        "videos": ["https://youtu.be/yJK2UZ2YkwA?si=qypxhGIitL1dVHqy"]
    },
    "r": {
        "description": "Curl your tongue slightly and let air pass over it to make the 'R' sound: 'rrr'. Try 'rabbit' or 'run'.",
        "videos": ["https://youtu.be/dgAwcWO72z0?si=RWCxQl7iVvqOdorR"]
    },
    "s": {
        "description": "Smile slightly and let air pass through your teeth to create the 'S' sound: 'sss'. Try 'sun' or 'sock'.",
        "videos": ["https://youtu.be/KRbxUiF2dkw?si=edi_6n9vSoE617vm"]
    },
    "t": {
        "description": "Place your tongue behind your upper front teeth and release quickly: 'tuh'. Try 'tiger' or 'tree'.",
        "videos": ["https://youtu.be/j1ia8QFUIyg?si=7fDdIwAEbIqH6ptY"]
    },
    "w": {
        "description": "Round your lips and push them forward slightly while voicing: 'wuh'. Try 'water' or 'wagon'.",
        "videos": ["https://youtu.be/WHP9rOFibd4?si=Y7kpptwgPiSWQBs5"]
    }
}

@app.route('/get_exercise', methods=['POST'])
def get_exercise():
    try:
        data = request.json
        inaccurate_words = data.get("words", [])  # List of words sent from iOS app

        results = []
        for word in inaccurate_words:
            phoneme = word[0].lower()  # Simplified phoneme matching (first letter)
            if phoneme in EXERCISES:
                exercise = EXERCISES[phoneme]
                results.append({
                    "word": word,
                    "phoneme": phoneme,
                    "exercise": exercise["description"],
                    "video": random.choice(exercise["videos"])
                })

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
