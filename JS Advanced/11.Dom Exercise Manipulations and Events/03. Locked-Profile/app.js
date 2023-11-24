    function lockedProfile() {
        //<input type="radio" name="user1Locked" value="lock" checked>

        let checkbox = document.querySelectorAll('div[class="profile"]')[0].
            querySelector('input[type="radio"][value="unlock"]');

        let profiles = document.querySelectorAll('div[class="profile"]')

        for (let profile of profiles) {
            let btn = profile.querySelector('button')
            btn.addEventListener('click', onClick)
        }


        function onClick(ev) {
            let current_btn = ev.target
            let current_profile = current_btn.parentElement
            let isUnlocked = current_profile.querySelector('input[type="radio"][value="unlock"]').checked;
            if (isUnlocked) {
                let hidden_part = current_profile.querySelector('div')

                if(current_btn.textContent === 'Show more'){
                    hidden_part.style.display = 'block'    
                    current_btn.textContent = 'Hide it'
                }
                else{   
                    hidden_part.style.display = 'none'
                    current_btn.textContent = 'Show more'
                }
            }
        }
    }