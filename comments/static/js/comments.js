document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM content loaded');


  var replyForm = document.getElementById('replyForm');
  if (replyForm) {
    replyForm.style.display = 'none';
  }

  // "Reply"
  document.querySelectorAll('.reply-link').forEach(function(replyLink) {
    replyLink.addEventListener('click', function(event) {
      event.preventDefault();
      var parentCommentId = replyLink.getAttribute('data-comment-id');
      document.getElementById('parentCommentId').value = parentCommentId;


      if (replyForm) {
        replyForm.style.display = 'block';
      }
    });
  });

});
