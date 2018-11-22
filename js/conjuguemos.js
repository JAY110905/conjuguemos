/**
 * Conjugates an infinitive
 * @param {string} v Verb
 * @param {int} p Person (1, 2, 3)
 * @param {string} t Tense
 * @param {int} n Number (1 for singular, 2 for plural) 
 */
function c(v,p,t,n) {
    window.return = '';
    // The endpint below is a patch for http://api.ultralingua.com/conjugations/spa/{verb} designed to bypass HTTPS restrictions
    $.get('https://n7pmb2qz12.execute-api.us-east-2.amazonaws.com/v1/' + v.toLowerCase(), function(data) {
        for(c in data) {
            if((c['partofspeech']['number'] == ((n==1)?'singular':'plural')) && (c['partofspeech']['person'] == (['','first','second','third'])[p]) && (c['partofspeech']['tense'] == t)) {
                window.return = c['surfaceform'];
                break;
            }
        }
    });
    return window.return;
}
/**
 * Checks whether or not an answer was just accepted
 * Returns false if no correct answer was detected, even if it isn't necessarily incorrect
 * That is, if no message is present, it returns false by default
 */
function check() {
    return !!$("#answer-field .bubble.correct").length;
}
/**
 * Answers the current question
 * @returns {boolean} The result of check()
 * @see {@link check}
 */
function answer(value){
    $("#answer-input").val(value);
    $("#check-button").click();
    return check();
}