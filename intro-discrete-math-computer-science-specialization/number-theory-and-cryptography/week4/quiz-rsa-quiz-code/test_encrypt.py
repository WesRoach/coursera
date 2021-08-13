import pytest

from rsa import (
    FastModularExponentiationBKM,
    PowMod,
    ConvertToInt,
    ConvertToStr,
    Encrypt,
    InvertModulo,
    Decrypt,
    DecipherSimple,
    DecipherSmallPrime,
    IntSqrt,
    DecipherSmallDiff,
    DecipherCommonDivisor,
    DecipherHastad,
)


@pytest.mark.parametrize(
    "b,k,m,expected",
    [
        (7, 7, 11, 9),
    ],  # black dont do itttttttttttttttttttttttttttttttttttttttt
)
def test_FastModularExponentiationBKM(b, k, m, expected):
    assert expected == FastModularExponentiationBKM(b, k, m)


@pytest.mark.parametrize(
    "b,e,m,expected",
    [
        (7, 13, 11, 2),
    ],  # black dont do ittttttttttttttttttttttttttttttttttttttt
)
def test_PowMod(b, e, m, expected):
    assert expected == PowMod(b, e, m)


@pytest.mark.parametrize(
    "message,expected",
    [
        ("Hello, World!", 5735816763073854918203775149089)
    ],  # black dont do ittttttttttttttttttttttttttttttttttttttt
)
def test_ConvertToInt(message, expected):
    assert expected == ConvertToInt(message)


@pytest.mark.parametrize(
    "m,expected",
    [
        (5735816763073854918203775149089, "Hello, World!")
    ],  # black dont do ittttttttttttttttttttttttttttttttttttttt
)
def test_ConvertToStr(m, expected):
    assert expected == ConvertToStr(m)


@pytest.mark.parametrize(
    "message,modulo,exponent,expected",
    [
        # p = 1000000007
        # q = 1000000009
        # exponent = 23917
        # modulo = p * q
        # message = "attack"
        ("attack", 1000000016000000063, 23917, 577821702011958447),
        ("attack", 101, 12, 78),
    ],  # avoid black formatting ...............................................
)
def test_Encrypt(message, modulo, exponent, expected):
    assert expected == Encrypt(message, modulo, exponent)


@pytest.mark.parametrize(
    "a,n,expected",
    [
        (3, 7, 5)
    ],  # avoid black formatting ...........................................
)
def test_InvertModulo(a, n, expected):
    assert expected == InvertModulo(a, n)


@pytest.mark.parametrize(
    "ciphertext,p,q,exponent,expected",
    [
        (577821702011958447, 1000000007, 1000000009, 23917, "attack")
    ],  # black don't do it
)
def test_Decrypt(ciphertext, p, q, exponent, expected):
    assert expected == Decrypt(ciphertext, p, q, exponent)


@pytest.mark.parametrize(
    "ciphertext,modulo,exponent,potential_messages,expected",
    [
        (78, 101, 12, ["attack", "don't attack", "wait"], "attack"),
        (95, 101, 12, ["attack", "don't attack", "wait"], "don't attack"),
        (54, 101, 12, ["attack", "don't attack", "wait"], "wait"),
        (81, 101, 12, ["attack", "don't attack", "wait"], "don't know"),
    ],
)
def test_DecipherSimple(
    ciphertext, modulo, exponent, potential_messages, expected
):
    assert expected == DecipherSimple(
        ciphertext, modulo, exponent, potential_messages
    )


@pytest.mark.slow
@pytest.mark.parametrize(
    "ciphertext,modulo,exponent,expected",
    [
        (
            1773488865857950936127070415107286811735036786757360876488901668828411065415319121739305112809023074111043494948978081751851444797671426477224221428915534085499185651993502038149646686545099252921036161028865989784470806731700777521041215564203613423323285066203840329997825032261425978638927438518035030191944107572667758243311046550229409822846149831396410991755012812007339251536452615590635223780672174679677196279304461931703846255925914845500897273821827255506913276266523704922524156943959725369352703672131222283682166791913172292046709244906816668026610802197814114770298014914576347693504969280551524366327904,
            101
            * 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387,
            239,
            "attack",
        )
    ],
)
def test_DecipherSmallPrime(ciphertext, modulo, exponent, expected):
    assert expected == DecipherSmallPrime(ciphertext, modulo, exponent)


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 1),
        (4, 2),
        (3, 1),
        (16, 4),
        (15, 3),
    ],  # black nah don't event start bro .................................
)
def test_IntSqrt(n, expected):
    assert expected == IntSqrt(n)


@pytest.mark.parametrize(
    "ciphertext,modulo,exponent,expected",
    [
        (48582223151298950, 1000000016000000063, 239, "attack"),
        (589481416272092637, 1000000108000001827, 239, "attack"),
        (67933640194055204, 1000005190003727269, 239, "attack"),
    ],  # black don't .....................................................
)
def test_DecipherSmallDiff(ciphertext, modulo, exponent, expected):
    assert expected == DecipherSmallDiff(ciphertext, modulo, exponent)


@pytest.mark.slow
@pytest.mark.parametrize(
    "first_ciphertext,first_modulo,first_exponent,second_ciphertext,"
    "second_modulo,second_exponent,expected",
    [
        (
            1773488865857950936127070415107286811735036786757360876488901668828411065415319121739305112809023074111043494948978081751851444797671426477224221428915534085499185651993502038149646686545099252921036161028865989784470806731700777521041215564203613423323285066203840329997825032261425978638927438518035030191944107572667758243311046550229409822846149831396410991755012812007339251536452615590635223780672174679677196279304461931703846255925914845500897273821827255506913276266523704922524156943959725369352703672131222283682166791913172292046709244906816668026610802197814114770298014914576347693504969280551524366327904,
            1848196043986652010112242726156984105384782509849268928493301350012366116017272795056361826212801005535988029938124687999118804704622570370079693974534137018837492217688825282689826376269645192247243668173794861829838167037191748020696507137362128974320761252693959238795091818210822437125705940348133047915996120389068504408863371194831504806673900783553345045273252809288512168025895825053252345331726884678657596180928640474620337030418357954183345914610559564337274897510138353332945462588009676396782489066857314018652551466945185216554886128961308079154676679366830037696876930064837328700753090578001863704987087,
            239,
            46208840796,
            101000000707,
            17,
            ("attack", "wait"),
        )
    ],
)
def test_DecipherCommonDivisor(
    first_ciphertext,
    first_modulo,
    first_exponent,
    second_ciphertext,
    second_modulo,
    second_exponent,
    expected,
):
    assert expected == DecipherCommonDivisor(
        first_ciphertext,
        first_modulo,
        first_exponent,
        second_ciphertext,
        second_modulo,
        second_exponent,
    )


@pytest.mark.parametrize(
    "first_ciphertext,first_modulo,second_ciphertext,second_modulo,expected",
    [
        (
            11481721827796125988080971449,
            523631656370745185641961785048490596607211047839379680209373,
            11481721827796125988080971449,
            830069156372432509928666201723843242135846274670597876182117,
            "attack",
        )
    ],
)
def test_DecipherHastad(
    first_ciphertext, first_modulo, second_ciphertext, second_modulo, expected
):
    assert expected == DecipherHastad(
        first_ciphertext, first_modulo, second_ciphertext, second_modulo
    )
