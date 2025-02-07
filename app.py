from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Sample database of articulation exercises
EXERCISES = {
     "b": {
        "description": "Practice the 'R' sound by growling like a lion: 'Rrrrrr'. Hold the sound and release it into the word.",
        "videos": ["https://youtu.be/746Aq0ndZy0?si=EmuuYVEZbgZtbQ-i"]
    },
    "c": {
        "description": "Say 'ssss' like a snake, then blend it into words.",
        "videos": ["https://youtu.be/0z80Zt66RcU?si=NetUjmYCsm41Td12"]
    },
    "d": {
        "description": "Lift your tongue to the roof of your mouth while saying 'L' slowly.",
        "videos": ["https://youtu.be/61xe97Nf8J4?si=WjGvdsIr2i_enTNU"]
    },
    "f": {
        "description": "Practice the 'R' sound by growling like a lion: 'Rrrrrr'. Hold the sound and release it into the word.",
        "videos": ["https://youtu.be/xA61MYdspgM?si=s7FekF9psGSRn3a8"]
    },
    "g": {
        "description": "Say 'ssss' like a snake, then blend it into words.",
        "videos": ["https://youtu.be/bSlb9yscpbw?si=6xDZemT5YZ7dzMZw"]
    },
    "h": {
        "description": "Lift your tongue to the roof of your mouth while saying 'L' slowly.",
        "videos": ["https://youtu.be/3-qJF9ZstLQ?si=b3ougOIk6Gb91dSi"]
    },
    "j": {
        "description": "Practice the 'R' sound by growling like a lion: 'Rrrrrr'. Hold the sound and release it into the word.",
        "videos": ["https://youtu.be/xETjN3Y24cQ?si=P_Ot9L-Yf9ixvYhR"]
    },
    "k": {
        "description": "Say 'ssss' like a snake, then blend it into words.",
        "videos": ["https://youtu.be/JwKKfHIpOX8?si=pXhlNBBs7eSgj6X4"]
    },
    "l": {
        "description": "Lift your tongue to the roof of your mouth while saying 'L' slowly.",
        "videos": ["https://youtu.be/_IAEg3igJVI?si=4XMyQmXSTzMWSHIU"]
    },

    "m": {
        "description": "Lift your tongue to the roof of your mouth while saying 'L' slowly.",
        "videos": ["https://youtu.be/0VCeITL8P4E?si=wkwYbJP8642lrXVI"]
    },
    "n": {
        "description": "Practice the 'R' sound by growling like a lion: 'Rrrrrr'. Hold the sound and release it into the word.",
        "videos": ["https://youtu.be/oun0cGPMHZQ?si=xTBBvMTDWhwDsmHo"]
    },
    "p": {
        "description": "Say 'ssss' like a snake, then blend it into words.",
        "videos": ["https://youtu.be/yJK2UZ2YkwA?si=qypxhGIitL1dVHqy"]
    },


    "r": {
        "description": "Practice the 'R' sound by growling like a lion: 'Rrrrrr'. Hold the sound and release it into the word.",
        "videos": ["https://www.youtube.com/watch?v=xyz123"]
    },
    "s": {
        "description": "Say 'ssss' like a snake, then blend it into words.",
        "videos": ["https://www.youtube.com/watch?v=abc456"]
    },
    "t": {
        "description": "Lift your tongue to the roof of your mouth while saying 'L' slowly.",
        "videos": ["https://www.youtube.com/watch?v=lmn789"]
    },
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
