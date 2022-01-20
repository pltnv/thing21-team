import json

from sqlalchemy import func

from app import db
from app.helper import AlchemyEncoder


class Track(db.Model):
    __tablename__ = "tracks"

    id = db.Column(db.Integer(), primary_key=True)
    label = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    cover = db.Column(db.String(), nullable=False)
    src = db.Column(db.String(), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Track %r>" % self.label

    @classmethod
    def get_random_tracks(cls, limit: int = None):
        names = set(column.name for column in cls.__table__.columns)
        tracks = []

        for track in Track.query.order_by(func.random()).limit(limit).all():
            track_dict = {name: getattr(track, name) for name in names}
            track_dict["liked"] = False
            track_dict["status"] = False
            tracks.append(track_dict)

        return tracks

    @classmethod
    def filter_by_label_or_author(cls, label: str, author: str):

        names = set(column.name for column in cls.__table__.columns)
        request = db.session.query(Track)
        request_all = []

        if label:
            request_all += (
                request.filter(Track.label.like("%{0}%".format(label))).limit(5).all()
            )
        if author:
            request_all += (
                request.filter(Track.author.like("%{0}%".format(author))).limit(5).all()
            )

        tracks = []

        for track in request_all:
            track_dict = {name: getattr(track, name) for name in names}
            track_dict["liked"] = False
            track_dict["status"] = False
            tracks.append(track_dict)

        return tracks


tracks = [
    Track(
        label="Колизей",
        author="Miyagi & Эндшпиль",
        cover="https://avatars.yandex.net/get-music-content/192707/caee8fe2.a.5571285-1/400x400",
        src="https://zaycev.net/musicset/dl/130ecc8485352191daf78aabb3bbe4aa/8317135.json",
        duration="267",
    ),
    Track(
        label="Море внтури меня",
        author="Ёлка",
        cover="https://avatars.yandex.net/get-music-content/38044/61a176e7.a.2580929-1/400x400",
        src="https://zaycev.net/musicset/dl/f03bb15130b835863c37343a840cbb46/4372389.json",
        duration="217",
    ),
    Track(
        label="Москва любит",
        author="Скриптонит",
        cover="https://avatars.yandex.net/get-music-content/1880735/fa6a6018.a.9684249-1/400x400",
        src="https://zaycev.net/musicset/dl/adcc42f7b1d2f4f6d81d66da10867b14/17053802.json",
        duration="205",
    ),
    Track(
        label="Химия",
        author="Mujuce",
        cover="https://avatars.yandex.net/get-music-content/38044/536524be.a.3319291-1/400x400",
        src="https://zaycev.net/musicset/dl/b49edaf1dfcd63d63a153ca86e14f6bb/17556589.json",
        duration="249",
    ),
    Track(
        label="ЯТЛ",
        author="Zivert",
        cover="https://avatars.yandex.net/get-music-content/2266607/671089b8.a.9781709-1/400x400",
        src="https://zaycev.net/musicset/dl/ec46eca07b35bbb7cd39bdeb89c2bb7c/17100468.json",
        duration="223",
    ),
    Track(
        label="Смертельная битва",
        author="Александр Пистолетов",
        cover="https://avatars.yandex.net/get-music-content/176019/60308c6e.a.5486834-1/400x400",
        src="https://zaycev.net/musicset/dl/8447875b54dd6a48abeec7f96a3bb376/1676934.json",
        duration="176",
    ),
    Track(
        label="Веснушки",
        author="NЮ",
        cover="https://avatars.yandex.net/get-music-content/97284/61040537.a.8958861-1/400x400",
        src="https://zaycev.net/musicset/dl/e016ba5bb55351f209b4c998df720df4/11762499.json",
        duration="193",
    ),
    Track(
        label="Вихiдний",
        author="Dzidzio",
        cover="https://avatars.yandex.net/get-music-content/113160/b64aaf93.a.5379866-1/400x400",
        src="https://zaycev.net/musicset/dl/03dc9a76eaf4b7f08d39bc083ef5907f/6981250.json",
        duration="177",
    ),
    Track(
        label="Родина",
        author="ДДТ",
        cover="https://avatars.yandex.net/get-music-content/34131/73fed284.a.168137-2/400x400",
        src="https://zaycev.net/musicset/dl/751e3ee2dc5d3d86e7e61f6428dcda5d/4328157.json",
        duration="280",
    ),
    Track(
        label="Витаминка",
        author="Тима Белорусских",
        cover="https://avatars.yandex.net/get-music-content/192707/ae216e9b.a.6721271-1/400x400",
        src="https://zaycev.net/musicset/dl/6b3a103dfb09a342d176b1ec00075138/8662842.json",
        duration="176",
    ),
    Track(
        label="Найду тебя",
        author="Тима Белорусских",
        cover="https://avatars.yandex.net/get-music-content/98892/93ce997e.a.8328662-1/400x400",
        src="https://zaycev.net/musicset/dl/9d4a14bafe201be1f8ae532e5f67d4a6/12074898.json",
        duration="204",
    ),
    Track(
        label="Pamamera",
        author="Зомб",
        cover="https://avatars.yandex.net/get-music-content/143117/383e5819.a.4984543-1/400x400",
        src="https://zaycev.net/musicset/dl/c770bda04866515efbc504a3fbba610a/6981087.json?spa=false",
        duration="217",
    ),
    Track(
        label="Даже не половина",
        author="Зомб",
        cover="https://avatars.yandex.net/get-music-content/98892/ce43773f.a.4688671-2/400x400",
        src="https://zaycev.net/musicset/dl/cc24de3e2085a09d3eba290196200c51/6131903.json?spa=false",
        duration="171",
    ),
    Track(
        label="Ja cie kocham",
        author="Dzidzio",
        cover="https://avatars.yandex.net/get-music-content/49707/b8ed1cb4.a.2671501-1/400x400",
        src="https://zaycev.net/musicset/dl/b052d08c34d96aae05f069a9f336d7c1/1503125.json?spa=false",
        duration="209",
    ),
    Track(
        label="Евродэнс",
        author="GSPD",
        cover="https://avatars.yandex.net/get-music-content/142001/213622e2.a.5017744-1/400x400",
        src="https://zaycev.net/musicset/dl/51234cf2ad4b8bbf9435ce3dc7c3cee6/8317131.json?spa=false",
        duration="219",
    ),
    Track(
        label="Дура",
        author="GSPD",
        cover="https://avatars.yandex.net/get-music-content/97284/10f0829f.a.4704140-1/400x400",
        src="https://zaycev.net/musicset/dl/872280208676cec19538d80cc6bef059/8661554.json?spa=false",
        duration="233",
    ),
    Track(
        label="220",
        author="GSPD",
        cover="https://avatars.yandex.net/get-music-content/149669/98e360e0.a.5355612-1/400x400",
        src="https://zaycev.net/musicset/dl/872280208676cec19538d80cc6bef059/8661554.json?spa=false",
        duration="233",
    ),
    Track(
        label="Детство",
        author="Rauf & Faik",
        cover="https://avatars.yandex.net/get-music-content/108289/3897ef8f.a.7204664-1/400x400",
        src="https://zaycev.net/musicset/dl/52d97aafaf772be9c23f5abc5bb4fed8/8453720.json?spa=false",
        duration="188",
    ),
    Track(
        label="Между строк",
        author="Rauf & Faik",
        cover="https://avatars.yandex.net/get-music-content/193823/659766b5.a.7374327-1/400x400",
        src="https://zaycev.net/musicset/dl/01e0a13c88f087c378dd7606b7a51bbf/10894942.json?spa=false",
        duration="159",
    ),
    Track(
        label="Сан сийлахь даймохк",
        author="Макка Межиева",
        cover="https://avatars.yandex.net/get-music-content/193823/5bb003dc.a.5250172-1/400x400",
        src="https://zaycev.net/musicset/dl/60e58d3a65cfd99a2be749e345e86c33/3963375.json?spa=false",
        duration="256",
    ),
    Track(
        label="Комета",
        author="JONY",
        cover="https://avatars.yandex.net/get-music-content/143117/3cf7b3fd.a.8750133-1/400x400",
        src="https://zaycev.net/musicset/dl/93f0eedb1b145c0e72e84c06bc1c794e/15148374.json?spa=false",
        duration="161",
    ),
    Track(
        label="Мадам",
        author="JONY",
        cover="https://avatars.yandex.net/get-music-content/1880735/b940a25b.a.10014397-1/400x400",
        src="https://zaycev.net/musicset/dl/6391d3e288286070462135b1e3764787/17179323.json?spa=false",
        duration="171",
    ),
    Track(
        label="Вся такая в белом",
        author="Ramil",
        cover="https://avatars.yandex.net/get-music-content/99892/65e377b1.a.7299979-1/400x400",
        src="https://zaycev.net/musicset/dl/2a789b4e0742f4b0daa6b87af49b567a/8878692.json?spa=false",
        duration="182",
    ),
    Track(
        label="Салам алейкум братьям",
        author="Ислам Итляшев",
        cover="https://avatars.yandex.net/get-music-content/99892/3ee92d14.a.9202049-1/400x400",
        src="https://zaycev.net/musicset/dl/580c448e3db0f32525f278858f0d20ba/16669848.json?spa=false",
        duration="177",
    ),
    Track(
        label="На моем аккаунте",
        author="Kizaru",
        cover="https://avatars.yandex.net/get-music-content/192707/4ff53943.a.4807750-1/400x400",
        src="https://zaycev.net/musicset/dl/6f9b9b189c5723cfdf4ff640ef7de3e1/6153841.json?spa=false",
        duration="105",
    ),
    Track(
        label="Оу щит",
        author="Kizaru",
        cover="https://avatars.yandex.net/get-music-content/175191/b4282a1b.a.5872619-1/400x400",
        src="https://zaycev.net/musicset/dl/5557818230c56cd192e875f0fe3cefe8/4427903.json?spa=false",
        duration="167",
    ),
    Track(
        label="MORGENSHTERN",
        author="РАТАТАТАТА",
        cover="https://avatars.yandex.net/get-music-content/2114230/0c897710.a.9647864-1/400x400",
        src="https://zaycev.net/musicset/dl/5448561766eee1684e7af86a3b59cbcd/16877860.json?spa=false",
        duration="118",
    ),
    Track(
        label="Мне пох",
        author="MORGENSHTERN",
        cover="https://avatars.yandex.net/get-music-content/2110367/cc904557.a.9163273-1/400x400",
        src="https://zaycev.net/musicset/dl/415c355ac8bff6a857f0cad33c99c6e9/16594073.json?spa=false",
        duration="158",
    ),
]
