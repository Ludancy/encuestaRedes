<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
<style type="text/css">
  :root {
    --red: #ff5e6d;
  }
  .bg_red{
    background: var(--red);
  }
  .bg_gray{
    background: #ebebeb;
  }
  .border_round{
    border-radius: 5px;
    border: 1px solid var(--red);
  }
  .btn_red{
    color: white !important;
    background: var(--red) !important;
    border: 1px solid var(--red);
    transition: .5s all ease;
  }
  .btn_red:hover{
    color: var(--red) !important;
    background: transparent !important;
    border: 1px solid var(--red);
    transition: .5s all ease;
  }
  .form_poll{
    border-radius: 5px;
    max-width: 600px;
    margin-right: auto;
    margin-left: auto;
    background: #eee;
   -webkit-box-shadow: 0px 0px 5px 2px rgba(0,0,0,0.39);
    box-shadow: 0px 0px 5px 2px rgba(0,0,0,0.39);
  }
  .form_p{
    padding: 15px;
  }
  #wave {
    position: relative;
    height: 70px;
    width: 600px;
    z-index: 1;
    background: var(--red);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;

  }
  #wave:before {
    content: "";
    display: block;
    position: absolute;
    border-radius: 100% 50%;
    width: 341px;
    height: 80px;
    background-color: #eee;
    right: 0px;
    top: 40px;
    z-index: -1;
  }
  #wave:after {
    content: "";
    display: block;
    position: absolute;
    border-radius: 100% 50%;
    width: 300px;
    height: 70px;
    background-color: var(--red);
    left: 0;
    top: 27px;
    z-index: -1;
  }
  input[type='radio']{
    -ms-transform: scale(1.5); /* IE 9 */
    -webkit-transform: scale(1.5); /* Chrome, Safari, Opera */
    transform: scale(1.5);
  }
  input[type='radio']:checked:after {
    width: 15px;
    height: 15px;
    border-radius: 15px;
    top: -4px;
    left: -1px;
    position: relative;
    background-color: var(--red);
    content: '';
    display: inline-block;
    visibility: visible;
    border: 2px solid white;
  }
  .form-control:focus {
    color: #495057;
    background-color: #fff;
    border-color: var(--red);
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgb(255 94 109 / 25%);
  }
  .btn.focus, .btn:focus {
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgb(255 94 109 / 25%);
  }
</style>
