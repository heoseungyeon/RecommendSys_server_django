from posting.models import *
from posting.serializers import *
def userPostCnt(user_id):
    users = User.object.all()
    for user in users:
        print(user)
        print(user.posting_cnt)
        if user.idx == int(user_id):
            print("발견0")
            user.posting_cnt+=1
            user.save()
            break

def currentPostId():
    post = UserPlaceHistory.objects.last()
    return post.idx

def insertUserPlaceHistory(request):
    print(request.data)
    serializer = UserPlaceHistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return True
    return False

def insertScore(request,imageScore,textScore):
    user_id = request.data.get('user_idx')

    #imageScoreUpdate
    for imageKey in imageScore.keys():
        categoryS = CategoryImageS.objects.all()
        for category in categoryS:
            if category.ctgr_name == imageKey:
                print("발견")
                small_id = category.ctgr_sid
                large_id = category.large_id.large_id.ctgr_lid
                middle_id = category.middle_id.ctgr_mid
                print(large_id,middle_id)
                #largeScore Update
                data=dict()
                data['user_idx']=user_id
                data['ctgr_idx']=large_id
                data['score']=imageScore.get(imageKey)
                data['posting_idx']=currentPostId()
                print("large_image:",data)
                serializer = UserLScoreSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                #MiddleScore Update
                data.clear()
                data['user_idx']=user_id
                data['image_ctgr_idx']=middle_id
                data['score']=imageScore.get(imageKey)
                data['posting_idx']=currentPostId()
                print("middle_image:", data)
                serializer = ImageMScoreSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                #SmallScore Update
                data.clear()
                data['user_idx']=user_id
                data['image_ctgr_idx']=small_id
                data['score']=imageScore.get(imageKey)
                data['posting_idx']=currentPostId()
                print("small_image:", data)
                serializer = ImageSScoreSerializer(data=data)
                if serializer.is_valid():
                    print("valid")
                    serializer.save()

    #TextScoreUpdate
    for textKey in textScore.keys():
        categoryS = CategoryTextS.objects.all()
        for category in categoryS:
            if category.ctgr_name == textKey:
                print("발견2")
                small_id = category.ctgr_id
                large_id = category.large_id.ctgr_lid
                middle_id = category.middle_id.ctgr_id
                #largeScore Update
                data=dict()
                data['user_idx']=user_id
                data['ctgr_idx']=large_id
                data['score']=textScore.get(textKey)
                data['posting_idx']=currentPostId()
                print("large_image:", data)
                serializer = UserLScoreSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                #MiddleScore Update
                data.clear()
                data['user_idx']=user_id
                data['text_ctgr_idx']=middle_id
                data['score']=textScore.get(textKey)
                data['posting_idx']=currentPostId()
                print("large_image:", data)
                serializer = TextMScoreSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                #SmallScore Update
                data.clear()
                data['user_idx']=user_id
                data['text_ctgr_idx']=small_id
                data['score']=textScore.get(textKey)
                data['posting_idx']=currentPostId()
                print("large_image:", data)
                serializer = TextSScoreSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()








