from zrb.builtin.eval_task import evaluate


def test_eval():
    main_loop = evaluate.create_main_loop()
    result = main_loop(text='1+1')
    assert result == '2'
