// Have to copy python logic to js
// Because for loop didn't work with window.open, 
// I made this questionable recursion method

// document.getElementById("search").addEventListener("onclick", search(-1,"","","","","",""));

var a = document.getElementById("search");

a.addEventListener('click',function(){
    search(-1);
});
function search(number, before_i, after_i, words_i, google, duckduckgo, bing){
    // These variables will be only inicilized / given value one time
    var before,after,words, google, duckduckgo, bing;
    // Number can be -1 only once, so this if statement is just for start of recursion
    if (number == -1){
    before = document.getElementById("before_input").value;
    after = document.getElementById("after_input").value;
    words = document.getElementById("words_input").value.split(' ');
    // Combine '+' in words into spaces (so you can call multiple words for multiple searches)
    combineWords(words);
    // number - how many times the function will be called (number of words)
    number = words.length;
    // Get values of checkboxes
    try{
    google =  document.querySelector('.google_checkbox:checked').value;}
    catch(e){}
    try{
    duckduckgo = document.querySelector('.duckduckgo_checkbox:checked').value;}
    catch(e){}
    try
    {bing = document.querySelector('.bing_checkbox:checked').value;}
    catch(e){}
    // If there are no words when button is pressed / no checkboxes clicked the recursion will end
    if (words == "" || (google != 'on' && duckduckgo != 'on' && bing != 'on')) number = 0;
    search(number, before, after, words, google, duckduckgo, bing);
    }
    else if(number > 0){
        // These values are always the same
        before = before_i;
        after = after_i;
        words = words_i;
        // Which checkboxes are ticked
        if(google == 'on'){
            window.open(
            "https://google.com/search?q=" + before + "+" + words[words.length - number] + "+" + after);}
        if(duckduckgo == 'on'){
        window.open(
            "https://duckduckgo.com/?q=" + before + "+" + words[words.length - number] + "+" + after);}

        if(bing == 'on'){
        window.open(
            "https://bing.com/search?q=" + before + "+" + words[words.length - number] + "+" + after);}
        // For recursion to go closer to zero
        number -= 1;
        // Recursion call
        search(number, before, after, words, google, duckduckgo, bing);
    }
}
// Function first checks if given words list include '+' and then replaces it with a space
function combineWords(words){
    for(let i = 0; i < words.length; i++){
        if (words[i].includes('+')) words[i] = words[i].replace("+", " ");
    }
}

// Clear currently written text

var b = document.getElementById("clear");

b.addEventListener('click',function(){
    clearContext();
});

function clearContext(){
    document.getElementById("before_input").value = "";
    document.getElementById("after_input").value = "";
    document.getElementById("words_input").value = "";
}