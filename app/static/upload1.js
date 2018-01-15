//---- custom js ----- //

// hide initial
$("#searching").hide();
$("#results-table").hide();
$("#error").hide();

// global
  var url = 'dataset/';
  var data = [];

  $(function() {

    // sanity check
    console.log( "ready!" );

    // image click
    $("#upload-file-btn").click(function() {

      // empty/hide results
      $("#uploaded_image").empty();
      $("#results").empty();
      $("#results-table").hide();
      $("#error").hide();

      // remove active class
      $(".img").removeClass("active")

      // add active class to clicked picture
      $(this).addClass("active")

      // grab image url
      var image = $(this).attr("src")

      // show searching text
      $("#searching").show();
      console.log("searching...")
var form_data = new FormData($('#upload-file')[0]);
      // ajax request
      $.ajax({
        type: "POST",
        url: "/upload",
        data : form_data,
        contentType: false,
        cache: false,
        processData: false,
        async: false,
        // handle success
        success: function(result) {
          console.log(result);
          var data = result.results
          var file = 'dataset1/'+result.file
          // show table
          $("#results-table").show();
          // loop through results, append to dom
          $("#uploaded_image").append('<img src ="'+file+'">')
          for (i = 0; i < data.length; i++) {

            $("#results").append('<tr><th><a href="'+url+data[i]["image"]+'"><img src="'+url+data[i]["image"]+
              '" class="result-img"></a></th><th>'+data[i]['score']+'</th></tr>')
          };
        },
        // handle error
        error: function(error) {
          console.log(error);
          // append to dom
          $("#error").append()
        }
      });


    });

  });
